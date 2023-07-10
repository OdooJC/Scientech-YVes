# -*- coding: utf-8 -*-

from itertools import groupby
from datetime import datetime, timedelta

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_is_zero, float_compare, DEFAULT_SERVER_DATETIME_FORMAT

class AccountPaymentInherit(models.Model):
	_inherit = "account.payment"

	loyalty_used_from_last = fields.Boolean(string='Used from last')

	def action_post(self):
		res = super(AccountPaymentInherit, self).action_post()

		move_id = self.env['account.move'].search([('name', '=', self.ref)])
		if move_id:
			amount_commissionable = sum(
				move_id.invoice_line_ids.filtered(
					lambda r: r.product_id.is_commissionable).mapped('price_subtotal'))

			point_cal = int(self.env['ir.config_parameter'].sudo().get_param('bi_sale_loyalty.point_cal'))
			
			loyalty_history = False
			if amount_commissionable and point_cal > 0 and self.partner_type == 'customer':
				new_loyalty = int(amount_commissionable / point_cal)
				if new_loyalty > 0:
					vals = {
						'payment_id':self.id,
						'partner_id': self.partner_id.id,
						'date' : datetime.now().date() ,
						'points': new_loyalty,
						'payment_amount' : amount_commissionable,
					}
					if self.payment_type == 'outbound':
						vals.update({
							'transaction_type' : 'send',
							'total_payment_amount' : self.partner_id.total_amount - amount_commissionable,
							'total_points': self.partner_id.loyalty_points - new_loyalty
						})
						if self.partner_id.last_yr_loyalty_points >= new_loyalty :
							vals.update({
								'used_from_last': True,
							})
							self.write({'loyalty_used_from_last': True})
						loyalty_history = self.env['loyalty.history'].create(vals)
					if self.payment_type == 'inbound':
						vals.update({
							'transaction_type' : 'receive',
							'total_payment_amount' : self.partner_id.total_amount + amount_commissionable,
							'total_points': self.partner_id.loyalty_points + new_loyalty,
						})
						loyalty_history = self.env['loyalty.history'].create(vals)
		return res


	def action_draft(self):
		res = super(AccountPaymentInherit, self).action_draft()
		point_cal = int(self.env['ir.config_parameter'].sudo().get_param('bi_sale_loyalty.point_cal'))
		
		if point_cal > 0 and self.partner_type == 'customer':
			new_loyalty = int(self.amount / point_cal)
			if new_loyalty > 0 :
				vals = {
					'payment_id':self.id,
					'partner_id': self.partner_id.id,
					'date' : datetime.now().date() ,
					'points': new_loyalty,
					'payment_amount' : self.amount,
					'transaction_type' : 'cancel',
					'total_points': self.partner_id.loyalty_points  - new_loyalty,
					'total_payment_amount' : self.partner_id.total_amount - self.amount,
				}
				if self.payment_type == 'outbound':
					vals.update({
						'is_send_cancel' : True,
						'total_points': self.partner_id.loyalty_points  +  new_loyalty,
						'total_payment_amount' : self.partner_id.total_amount + self.amount,
					})
					if self.loyalty_used_from_last :
						vals.update({
							'last_year_used_cancel' : True,
						})
				loyalty_history = self.env['loyalty.history'].create(vals)
		return res
