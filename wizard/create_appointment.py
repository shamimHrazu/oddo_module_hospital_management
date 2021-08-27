from odoo import api,models, fields , _


class CreateAppointmentWizard(models.TransientModel):
    _name = "create.appointment.wizard"
    _description = "Create Appointment Wizard"
    appointment_date = fields.Date(string="Appointment Date & Time ")
    patient_id = fields.Many2one('hospital.patient' , string= "patient id", tracking = True, required = True)
    state = fields.Selection([
                              ('confirm', 'Confirmed'),],
                             string="status", tracking=True)

    def action_appointment_confirm(self):
        vals = {
            'patient_id' : self.patient_id.id ,
            'date_appointment' : self.appointment_date,
        }
        self.env['hospital.patient.appointment'].create(vals)
