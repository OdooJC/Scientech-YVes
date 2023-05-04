# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResCompany(models.Model):
    _name = 'res.company'
    _inherit = ['res.company', 'l10n_cl.counties.mixin']

    city_id = fields.Many2one(
        "res.city", string="Commune",
        compute='_get_current_city', inverse='_set_current_city',
        help="Commune of the company")

    def _get_current_city(self):
        """Get the city of the related partner."""
        self.city_id = self.partner_id.city_id

    def _set_current_city(self):
        """Set the city on the related partner."""
        self.partner_id.city_id = self.city_id

    @api.onchange('city_id')
    def _onchange_city_id(self):
        """Autocomplete the address based on a selected city."""
        self.full_city_address()
