from odoo import models, fields
class PartnerHistory(models.Model):
    _name = 'partner.history'

    name = fields.Char('Name')
    date = fields.Date('Date')
    partner_id = fields.Many2one('res.partner','Partner')

    def create_history(self):

        new_context = dict(self.env.context)
        if 'active_id' not in new_context.keys():
            new_context.update({'active_id': self.id, 'active_model': 'partner.history'})
        action = self.env['ir.actions.server'].browse(1217)
        recs = action.with_context(new_context)
        recs.run()

        print "executing..............server action",action
        return {'type':'ir.actions.client',
            'tag':'form-reload'
            }

class ResPartner(models.Model):
    _inherit = 'res.partner'

    history_ids = fields.One2many('partner.history','partner_id','History')
