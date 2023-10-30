from odoo import models, fields, api


class ResPartner(models.Model):
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
            state = partner.state_id
            if state:
                state_code = state.code
                if state_code in [
                    "CL01000",
                    "CL01100",
                    "CL01400",
                    "CL02000",
                    "CL02100",
                    "CL02200",
                    "CL02300",
                    "CL03000",
                    "CL03100",
                    "CL03200",
                    "CL03300",
                    "CL04000",
                    "CL04100",
                    "CL04200",
                    "CL04300",
                    "CL15000",
                    "CL15100",
                    "CL15200",
                ]:
                    partner.zona_clasificacion = "zona_norte"
                elif state_code in [
                    "CL05000",
                    "CL05100",
                    "CL05200",
                    "CL05300",
                    "CL05400",
                    "CL05500",
                    "CL05600",
                    "CL05700",
                    "CL06000",
                    "CL06100",
                    "CL06200",
                    "CL06300",
                    "CL07000",
                    "CL07100",
                    "CL07200",
                    "CL07300",
                    "CL07400",
                ]:
                    partner.zona_clasificacion = "zona_centro"
                elif state_code in [
                    "CL08000",
                    "CL08100",
                    "CL08200",
                    "CL08300",
                    "CL09000",
                    "CL09100",
                    "CL09200",
                    "CL10000",
                    "CL10100",
                    "CL10200",
                    "CL10300",
                    "CL10400",
                ]:
                    partner.zona_clasificacion = "zona_sur_1"
                elif state_code in [
                    "CL11000",
                    "CL11100",
                    "CL11200",
                    "CL11300",
                    "CL11400",
                    "CL12000",
                    "CL12100",
                    "CL12200",
                    "CL12300",
                    "CL12400",
                    "CL16000",
                ]:
                    partner.zona_clasificacion = "zona_sur_2"
                elif state_code in [
                    "CL13000",
                    "CL13100",
                    "CL13200",
                    "CL13300",
                    "CL13400",
                    "CL13500",
                    "CL13600",
                    "CL14000",
                    "CL14100",
                    "CL14200",
                ]:
                    partner.zona_clasificacion = "zona_metropolitana"
                else:
                    partner.zona_clasificacion = False
            else:
                partner.zona_clasificacion = False
