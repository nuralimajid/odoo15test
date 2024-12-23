
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
    
    @api.onchange('country_id')
    def _onchange_country_id(self):
        if self.country_id:
            state = self.env['res.country.state'].search([('country_id','=',self.country_id.id)], limit =1)
            self.state_id = state.id
