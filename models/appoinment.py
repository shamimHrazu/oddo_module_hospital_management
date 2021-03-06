from odoo import fields, api,models, _
from odoo.exceptions import ValidationError


class PatientAppoinment(models.Model):
    _name = "hospital.patient.appointment"
    _description = "Patient Appointment Schedule"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = "id desc"
    name = fields.Char(string='appointment_id', required=True, copy=False, readonly=True, default=lambda self: _('New'))
    patient_id = fields.Many2one('hospital.patient' , string= "patient id", tracking = True)
    state = fields.Selection([('draft', 'Draft'),
                              ('confirm', 'Confirmed'),
                              ('done', 'Done'),
                              ('cancel', 'Canceled')],
                             string="status", default="draft", tracking=True)
    name = fields.Char(string='Reference', required=True, copy=False, readonly=True, default=lambda self: _('New'))
    note = fields.Text(string="Description",tracking=True)
    date_appointment = fields.Date(string="Appointment Date")
    doctor_id = fields.Many2one('hospital.doctor', string="Consultant", tracking = True)
    checkup_time = fields.Datetime(string="Check Up Time")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string='Gender', required=True, copy=False, default='male', tracking=True)
    prescription = fields.Text(string="doctor's prescription")
    lab_test = fields.Selection([
        ('cpd', 'CPD test'),
        ('bilirubin', 'BIlirubin'),
    ])
    medicine_list_ids = fields.One2many('prescription.medicine','appointment_id', string="prescription line")
    def action_button_confirm(self):
        print("Confirm Button Clicked")
        self.state='confirm'

    def action_button_done(self):
        print("Done button clicked")
        self.state='done'

    def action_button_draft(self):
        self.state = 'draft'

    def action_button_cancel(self):
        self.state="cancel"

    @api.model
    def create(self, vals_list):
        if not vals_list.get('note'):
            vals_list['note'] = 'new patient'
        if vals_list.get('name', _('New')) == _('New'):
            vals_list['name'] = self.env['ir.sequence'].next_by_code('hospital.patient.appointment') or _('New')
        res = super(PatientAppoinment, self).create(vals_list)
        return res

    @api.onchange('patient_id')
    def _onchange_patient_id(self):
        if self.patient_id:
            self.gender = self.patient_id.gender

        if self.note:
            self.note = self.patient_id.note
        else:
            self.note = 'New Patient'

    def unlink(self):
        if self.state == 'done':
            raise ValidationError(_('you can not delete %s as it is in done state')%self.name)
        return super(PatientAppoinment, self).unlink()


class Medicine(models.Model):
    _name = "prescription.medicine"
    _description = "medicine list"

    name = fields.Char(string="Medicine name")
    qty = fields.Integer()
    times = fields.Integer()
    note = fields.Text()
    appointment_id = fields.Many2one('hospital.patient.appointment', string="appointment id")

