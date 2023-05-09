# -*- coding: utf-8 -*-

from odoo import fields, models


class CrmLead(models.Model):
    _inherit = "crm.lead"

    sale_channel_id = fields.Many2one(
        "sale.channel", ondelete="restrict",
        help="It's used to specify which channel an opportunity"
        " comes from.")

    def action_new_quotation(self):
        res = super().action_new_quotation()
        if self.sale_channel_id:
            res['context']['default_sale_channel_id'] =\
                self.sale_channel_id.id
        return res
