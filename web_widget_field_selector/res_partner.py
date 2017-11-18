from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    model_id = fields.Selection(selection='_list_all_models', string='Model', required=False)

    @api.model
    def _list_all_models(self):
        self._cr.execute("SELECT model, name FROM ir_model ORDER BY name")
        return self._cr.fetchall()
