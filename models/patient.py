from odoo import api, fields, models, _


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
    reference = fields.Char(string='Reference', required=True, copy=False, readonly=True, default=lambda self: _('New'))
    appointment_count = fields.Integer(string="appointment count", compute = "_compute_appointment_count")
    state = fields.Selection([('draft', 'Draft'),
                              ('confirm', 'Confirmed'),
                              ('done', 'Done'),
                              ('cancel', 'Canceled')],
                             string="status" ,default="draft", tracking= True)
    appointed_doctor_id = fields.Many2one('hospital.doctor', string="Consultant", tracking = True)
    image = fields.Binary(string="Patient image")
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

    @api.model
    def create(self,vals_list):
        if not vals_list.get('note'):
            vals_list['note'] = 'new patient'
        if vals_list.get('reference', _('New')) == _('New'):
            vals_list['reference'] = self.env['ir.sequence'].next_by_code('hospital.patient') or _('New')
        res = super(HospitalPatient, self).create(vals_list)
        return res

    def _compute_appointment_count(self):
        for rec in self:
            ac = self.env['hospital.patient.appointment'].search_count([('patient_id' , '=' , rec.id)])
            rec.appointment_count = ac

    @api.model
    def default_get(self, fields_list):
        res = super(HospitalPatient,self).default_get(fields_list)
        print(fields_list)
        print(res)
        res['gender'] = 'female'
        res['age'] = 18
        if not res.get('note'):
            res['note'] = "type a description"
        return res
