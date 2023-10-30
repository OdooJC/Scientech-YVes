from odoo import models, fields, api


class ResPartnerExtension(models.Model):
    _inherit = "res.partner"

    zona_clasificacion = fields.Selection(
        [
            ("zona_norte", "Zona Norte"),
            ("zona_centro", "Zona Centro"),
            ("zona_sur_1", "Zona Sur 1"),
            ("zona_sur_2", "Zona Sur 2"),
            ("zona_metropolitana", "Zona Metropolitana"),
        ],
        string="Zona de Clasificación",
        compute="_compute_zona_clasificacion",
        store=True,
    )

    @api.depends("state_id")
    def _compute_zona_clasificacion(self):
        for partner in self:
            if partner.state_id:
                state_code = partner.state_id.code
                if state_code in (
                    "CL01000",
                    "CL02000",
                    "CL03000",
                    "CL04000",
                    "CL15000",
                ):
                    partner.zona_clasificacion = "zona_norte"
                elif state_code in ("CL05000", "CL06000", "CL07000"):
                    partner.zona_clasificacion = "zona_centro"
                elif state_code in ("CL09000", "CL10000"):
                    partner.zona_clasificacion = "zona_sur_1"
                elif state_code in ("CL11000", "CL12000"):
                    partner.zona_clasificacion = "zona_sur_2"
                elif state_code == "CL13000":
                    partner.zona_clasificacion = "zona_metropolitana"
                else:
                    partner.zona_clasificacion = False
