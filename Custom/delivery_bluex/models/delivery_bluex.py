# -*- coding: utf-8 -*-

from odoo import fields, models, _


class ProviderBluex(models.Model):
    _inherit = 'delivery.carrier'

    delivery_type = fields.Selection(selection_add=[
        ('bluex', "Bluexpress")
    ], ondelete={'bluex': lambda recs: recs.write({'delivery_type': 'fixed', 'fixed_price': 0})})

    def bluex_get_tracking_link(self, picking):
        return 'https://www.blue.cl/seguimiento'

    def bluex_rate_shipment(self, order):
        return {'success': False,
                'price': 0.0,
                'error_message': _('This feature is not available yet.'),
                'warning_message': False}
