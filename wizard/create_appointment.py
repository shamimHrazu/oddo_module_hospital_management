from odoo import api,models, fields , _


class CreateAppointmentWizard(models.TransientModel):
    _name = "create.appointment.wizard"
    _description = "Create Appointment Wizard"

    name = fields.Char(string="Appointment for patient", required = True)
    patient_id = fields.Many2one('hospital.patient' , string= "patient id", tracking = True)
    state = fields.Selection([
                              ('confirm', 'Confirmed'),],
                             string="status", tracking=True)

    def action_button_confirm(self):
        self.state = 'confirm'
