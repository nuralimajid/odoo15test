from odoo import api, models, fields

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description="Hospital Patient"

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    gender = fields.Selection([
        ('male','Male'),
        ('female','Female'),
        ('other','Other')
    ], string="Gender", default="Other")
    age = fields.Integer(string="Age", default=0)
