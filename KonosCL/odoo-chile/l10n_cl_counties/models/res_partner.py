# -*- coding: utf-8 -*-

from odoo import api, models


class ResPartner(models.Model):
    _name = 'res.partner'
    _inherit = ['res.partner', 'l10n_cl.counties.mixin']

    @api.onchange('city_id')
    def _onchange_city_id(self):
        """Autocomplete the address based on a selected city.

        This method overwrites the original _onchange method provided by
        the base_address_city module.
        """
        self.full_city_address()
