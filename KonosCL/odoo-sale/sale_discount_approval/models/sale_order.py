# -*- coding: utf-8 -*-

from odoo import fields, models, _
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def need_disc_approval(self):
        """Returns True if any of the sales order lines contain a discount
        that exceeds the maximum value allowed; otherwise returns False"""
        icp = self.env['ir.config_parameter'].sudo()
        approval = icp.get_param('discount_approval', default=False)
        max_value = float(icp.get_param('max_discount_pct', default=0.0))
        if approval and max_value:
            return any([line.discount > max_value for line in self.order_line])
        return False

    def action_confirm(self):
        """Hack to send the sales order to the 'To Approve' stage when a
        discount on sale lines exceeds the maximum value allowed"""
        for order in self:
            if order.state not in ['draft', 'sent', 'to_approve']:
                continue
            if order.state == 'to_approve' and not order.user_has_groups(
                    'sale_order_approval.sales_approval_group'):
                raise ValidationError(
                    _("You do not have permission to confirm this sale order. "
                      "Please, contact your supervisor."))
            if not order.need_disc_approval()\
                    or (order.need_disc_approval() and order.user_has_groups(
                            'sale_order_approval.sales_approval_group')):
                return super(SaleOrder, self).action_confirm()
            else:
                order.write({'state': 'to_approve'})
                order.approval_notice()
