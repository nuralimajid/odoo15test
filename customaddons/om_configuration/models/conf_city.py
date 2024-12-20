
from odoo import models, fields, api

class ConfigurationCity(models.Model):
    _name = 'configuration.city'
    _description = 'City Configuration'
    _rec_name = 'name'
    
    name = fields.Char(string='City Name', required=True)
    code = fields.Char(string='City Code')
    state_id = fields.Many2one('res.country.state', string='State', required=True)
    country_id = fields.Many2one('res.country', string='Country', required=True)
    active = fields.Boolean(string='Active', default=True)
    
    @api.onchange('state_id')
    def _onchange_state_id(self):
        if self.state_id:
            self.country_id = self.state_id.country_id.id
