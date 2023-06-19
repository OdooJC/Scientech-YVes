# -*- coding: utf-8 -*-

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    credit_limit = fields.Float(
        tracking=True,
        help="The maximum credit allowed for this partner.")
    include_sales = fields.Boolean(
        string="Include Sales Orders?", tracking=True,
        help="If enabled, the sales orders will be included as part of the "
        "computation for the credit limit.")
