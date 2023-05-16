# -*- coding: utf-8 -*-

from odoo import api, fields, models


class CrmLead(models.Model):
    _name = 'crm.lead'
    _inherit = ['crm.lead', 'l10n_cl.counties.mixin']

    city_id = fields.Many2one(
        "res.city", string="Commune",
        help="Commune of the lead")

    @api.onchange('city_id')
    def _onchange_city_id(self):
        """Autocomplete the address based on a selected city."""
        self.full_city_address()

    @api.model
    def create(self, values):
        """Autocomplete the address in the case that only the city
        has been provided."""
        res = super().create(values)
        target_id = self.env.ref('base.cl')
        if res.country_id.id == target_id.id and res.city_id\
                and not res.state_id and not res.city:
            res.full_city_address()
        return res
