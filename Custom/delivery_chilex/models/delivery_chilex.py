# -*- coding: utf-8 -*-

from odoo import fields, models, _


class ProviderChilex(models.Model):
    _inherit = 'delivery.carrier'

    delivery_type = fields.Selection(selection_add=[
        ('chilex', "Chilexpress")
    ], ondelete={'chilex': lambda recs: recs.write({'delivery_type': 'fixed', 'fixed_price': 0})})

    def chilex_get_tracking_link(self, picking):
        return 'https://www.chilexpress.cl/estado-envio-paquete-courier'

    def chilex_rate_shipment(self, order):
        return {'success': False,
                'price': 0.0,
                'error_message': _('This feature is not available yet.'),
                'warning_message': False}
