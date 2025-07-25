from odoo import models, fields, api

class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Hospital Appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'ref' 
    

    patient_id = fields.Many2one('hospital.patient', string='Patient')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], string='Gender', related='patient_id.gender')
    appointment_time = fields.Datetime(string='Appointment Time', default=fields.Datetime.now)
    booking_date = fields.Date(string='Booking Date', default=fields.Date.context_today)
    ref = fields.Char(string='Reference')
    doctor_id = fields.Many2one('res.users', string='Doctor')
    prescription = fields.Html(string='Prescription')

    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'Medium'),
        ('3', 'High'),
        ('4', 'Very High'),
    ], string='Priority')
    
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'In Consultation'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ], string='Status', default='draft', required=True)

    pharmacy_line_ids = fields.One2many(
        'appointment.pharmacy.lines', 'appointment_id', string='Pharmacy Lines')
    hide_sales_price = fields.Boolean(string='Hide Sales Price')




    @api.onchange('patient_id')
    def _onchange_patient_id(self):
        self.ref = self.patient_id.ref
        
    def action_test(self):
        print("Test Button Clicked")
        return {
        "effect": {
            "fadeout": "slow",
            "message": "Click Successfully!",
            "type": "rainbow_man"
        }
    }
        
    def action_in_consultation(self):
        for rec in self:
            rec.state = 'in_consultation'
            
    def action_done(self):
        for rec in self:
            rec.state = 'done'
            
    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'
    
    def action_draft(self):
        for rec in self:
            rec.state = 'draft'
            
            
class  AppointmentPharmacyLines(models.Model):
    _name = 'appointment.pharmacy.lines'
    _description = 'Appointment Pharmacy Lines'


    product_id = fields.Many2one('product.product', string='Product', required=True)
    qty = fields.Float(string='Quantity', default=1.0)
    price_unit = fields.Float(related='product_id.list_price', string='Price')
    appointment_id = fields.Many2one('hospital.appointment', string='Appointment')




