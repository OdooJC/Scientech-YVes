# -*- coding: utf-8 -*-

from odoo import api, models


class L10nClCountiesMixin(models.AbstractModel):
    _name = 'l10n_cl.counties.mixin'
    _description = 'Useful methods for addresses'

    def full_city_address(self):
        """Autocomplete the address based on a selected city.

        This feature is used for both companies and partners because full
        address information must be provided to avoid potential problems
        when generating electronic invoices.
        """
        address = dict.fromkeys(['city', 'zip', 'state'], False)
        if self.city_id:
            parent_id = self.city_id.state_id.parent_id
            address.update({
                'city': self.city_id.state_id.name,
                'state':
                    parent_id.id if parent_id else self.city_id.state_id.id,
                'zip': self.city_id.zipcode,
            })
        self.city = address.get('city')
        self.state_id = address.get('state')
        self.zip = address.get('zip')
