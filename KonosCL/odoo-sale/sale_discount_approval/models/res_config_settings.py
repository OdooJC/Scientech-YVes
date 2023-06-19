# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    discount_approval = fields.Boolean(
        string="Approval of discounts",
        config_parameter='discount_approval',
        help="Managers must approve discounts granted on sales order lines")
    max_discount_pct = fields.Float(
        string="Discount Value",
        config_parameter='max_discount_pct',
        help="The maximum value allowed for discounts on sales order lines "
        "without a manager approval")

    @api.onchange('group_discount_per_so_line')
    def _onchange_group_discount_per_so_line(self):
        """Clears parameter values whenever the discount is disabled"""
        if hasattr(
                super(ResConfigSettings, self),
                '_onchange_group_discount_per_so_line'):
            super(
                ResConfigSettings, self)._onchange_group_discount_per_so_line()
        if not self.group_discount_per_so_line:
            self.update({
                'max_discount_pct': 0.0,
                'discount_approval': False,
            })
