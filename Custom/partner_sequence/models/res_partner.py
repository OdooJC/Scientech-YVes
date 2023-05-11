# -*- coding: utf-8 -*-

from odoo import api, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    # Although it is not a good practice, the fields already created
    # previously through Odoo Studio were used because they affected
    # other fields (also created with Odoo Studio) so in the end it
    # was not feasible to migrate all the fields to this particular
    # module

    def _get_next_ref(self):
        return self.env["ir.sequence"].next_by_code("res.partner") or '/'

    @api.model
    def create(self, vals):
        if not vals.get("x_studio_socio") and\
                vals.get("x_studio_cliente_individual") == 'Socio':
            vals["x_studio_socio"] = self._get_next_ref()
        return super().create(vals)

    def copy(self, default=None):
        default = default or {}
        if self.x_studio_cliente_individual == 'Socio':
            default["x_studio_socio"] = self._get_next_ref()
        return super().copy(default=default)

    def write(self, vals):
        for partner in self:
            vals_copy = vals.copy()
            if vals_copy.get("x_studio_cliente_individual") == 'Socio' and\
                    not vals_copy.get("x_studio_socio") and\
                        not partner.x_studio_socio:
                vals_copy["x_studio_socio"] = partner._get_next_ref()
            super().write(vals_copy)
        return True
