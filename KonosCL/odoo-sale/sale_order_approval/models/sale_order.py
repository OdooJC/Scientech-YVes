# -*- coding: utf-8 -*-

from odoo import fields, models, _
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    state = fields.Selection(selection_add=[
        ('to_approve', 'To Approve'), ('sale',)])

    def need_approval(self):
        """Verifies the partner available credit limit and return True if
        the order amount exceeds it; otherwise, returns False"""
        excess = False
        partner = self.partner_id

        if not partner.credit_limit:
            return excess

        total_due = partner.total_due
        if partner.include_sales:
            order_ids = self.env['sale.order'].search([
                ('id', '!=', self.id),
                ('partner_id', '=', partner.id),
                ('state', 'in', ['sent', 'sale']),
                ('invoice_status', '!=', 'invoiced'),
            ])
            total_due += sum([order.amount_total for order in order_ids])
        available_credit = partner.credit_limit - total_due

        if self.amount_total > available_credit:
            excess = True
        return excess

    def approval_notice(self):
        """Send an email to all authorized users to notify the existence of
        a sales order awaiting for approval"""
        mail_template = self.env.ref(
            'sale_order_approval.approval_notice_template')
        group = self.env.ref(
            'sale_order_approval.sales_approval_group')
        users = self.env['res.users'].search([('groups_id', '=', group.id)])
        if users and mail_template:
            email_values = {
                'email_to': ','.join(
                    [user.login for user in users])}
            for record in self:
                mail_template.send_mail(record.id, email_values=email_values)

    def action_confirm(self):
        """Hack to send the sales order to the 'To Approve' stage when the
        order amount exceeds the partner credit limit"""
        for order in self:
            if order.state not in ['draft', 'sent', 'to_approve']:
                continue

            if order.state == 'to_approve' and not order.user_has_groups(
                    'sale_order_approval.sales_approval_group'):
                raise ValidationError(
                    _("You do not have permission to confirm this sale order. "
                      "Please, contact your supervisor."))

            if not order.need_approval()\
                    or (order.need_approval() and order.user_has_groups(
                            'sale_order_approval.sales_approval_group')):
                return super(SaleOrder, self).action_confirm()
            else:
                order.write({'state': 'to_approve'})
                order.approval_notice()
