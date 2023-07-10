# -*- coding: utf-8 -*-

from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    potential_loyalty_points = fields.Integer(
        compute="_compute_potential_loyalty_points",
        help="Points that can be accumulated for this sales order")

    @api.depends("order_line")
    def _compute_potential_loyalty_points(self):
        for record in self:
            if record.amount_untaxed < 0:
                record.potential_loyalty_points = 0
            else:
                line_ids = record.order_line.filtered(
                    lambda r: r.product_id.is_commissionable)
                if line_ids:
                    amount = sum(line_ids.mapped('price_subtotal'))
                    point_cal = int(
                        self.env['ir.config_parameter'].sudo().get_param(
                            'bi_sale_loyalty.point_cal'))
                    record.potential_loyalty_points = int(amount / point_cal)
                else:
                    record.potential_loyalty_points = 0
