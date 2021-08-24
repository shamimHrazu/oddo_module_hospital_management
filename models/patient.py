from odoo import api, fields, models


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "patient record"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Patients Name", required="true", tracking= True)
    age = fields.Integer(string="Age", tracking= True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string='Gender',  required=True, copy=False, default= 'male', tracking= True)
    note = fields.Text(string="Description", tracking= True)

    state = fields.Selection([('draft', 'Draft'),
                              ('confirm', 'Confirmed'),
                              ('done', 'Done'),
                              ('cancel', 'Canceled')],
                             string="status" ,default="draft", tracking= True)
    appointed_doctor_id = fields.Many2one('hospital.doctor', string="Consultant")

    def action_button_confirm(self):
        print("Confirm Button Clicked")
        self.state='confirm'
    def action_button_done(self):
        print("Done button clicked")
        self.state='done'
    def action_button_draft(self):
        self.state= 'draft'
    def action_button_cancel(self):
        self.state="cancel"
