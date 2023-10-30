from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = "res.partner"

    zona_clasificacion = fields.Selection(
        selection=[
            ("Zona Norte", "Zona Norte"),
            ("Zona Centro", "Zona Centro"),
            ("Zona Sur 1", "Zona Sur 1"),
            ("Zona Sur 2", "Zona Sur 2"),
            ("Zona Metropolitana", "Zona Metropolitana"),
        ],
        string="Zona de Clasificación",
        help="Seleccione la clasificación correspondiente.",
        store=True,
        index=True,
    )

    @api.onchange("state_id")
    def _onchange_state_id(self):
        if self.state_id:
            state_name = self.state_id.name

            if state_name in (
                "Arica y Parinacota",
                "Tarapacá",
                "Antofagasta",
                "Atacama",
                "Coquimbo",
            ):
                self.zona_clasificacion = "Zona Norte"
            elif state_name in (
                "Valparaíso",
                "del Libertador Gral. Bernardo O'higgins",
                "del Maule",
            ):
                self.zona_clasificacion = "Zona Centro"
            elif state_name in ("del Ñuble", "del BíoBio", "de la Araucania"):
                self.zona_clasificacion = "Zona Sur 1"
            elif state_name in (
                "Los Ríos",
                "de los Lagos",
                "Aysén del Gral. Carlos Ibáñez del Campo",
                "Magallanes",
            ):
                self.zona_clasificacion = "Zona Sur 2"
            elif state_name == "Metropolitana":
                self.zona_clasificacion = "Zona Metropolitana"
            else:
                self.zona_clasificacion = False
