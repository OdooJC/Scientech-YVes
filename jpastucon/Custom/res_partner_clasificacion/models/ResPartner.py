from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    x_studio_clasificacion = fields.Selection(
        selection=[
            ('orquidea', 'Orquídea'),
            ('gardenia', 'Gardenia'),
            ('margarita', 'Margarita'),
            ('hortencia', 'Hortensia'),
            ('lavanda', 'Lavanda'),
            ('capullo', 'Capullo'),
            ('sin_compra', 'Sin Compra'),
            ('recuperar', 'Recuperar'),
            ('eliminado', 'Eliminado'),
            ('empresa', 'Empresa'),
            ('tulipanes', 'Tulipanes'),
            ('publico', 'Público'),
            ('girasol', 'Girasol'),
        ],
        string='Clasificación',
        help='Seleccione la clasificación correspondiente.',
        store=True,
        index=True
    )
