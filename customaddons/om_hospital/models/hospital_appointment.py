from odoo import api, fields, models


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _description = "Hospital Appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = "id desc"

    name = fields.Char(string='Appointment Reference', required=True, copy=False, readonly=True,
                      default=lambda self: ('New'))
    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor', required=True)
    appointment_time = fields.Datetime(string='Appointment Time', required=True)
    booking_date = fields.Date(string='Booking Date', required=True, default=fields.Date.context_today)
    prescription = fields.Text(string='Prescription')
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High')], string="Priority")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')], default='draft', string="Status", tracking=True)

    @api.model
    def create(self, vals):
        if vals.get('name', ('New')) == ('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('hospital.appointment') or ('New')
        result = super(HospitalAppointment, self).create(vals)
        return result
    # Metode untuk mengubah status ke Confirmed
    def action_confirm(self):
        self.write({'state': 'confirm'})

    # Metode untuk mengubah status ke Done
    def action_done(self):
        self.write({'state': 'done'})

    # Metode untuk mengubah status ke Cancelled
    def action_cancel(self):
        self.write({'state': 'cancel'})

    # Metode untuk mengubah status kembali ke Draft
    def action_draft(self):
        self.write({'state': 'draft'})