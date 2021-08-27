from odoo import api,models, fields , _


class CreateAppointmentWizard(models.TransientModel):
    _name = "create.appointment.wizard"
    _description = "Create Appointment Wizard"
    appointment_date = fields.Date(string="Appointment Date & Time ")
    patient_id = fields.Many2one('hospital.patient' , string= "patient id", tracking = True, required = True)
    state = fields.Selection([
                              ('confirm', 'Confirmed'),],
                          string="status", tracking=True)

    #return view
    def action_appointment_confirm(self):
        vals = {
            'patient_id' : self.patient_id.id ,
            'date_appointment' : self.appointment_date,
        }
        appointment_id = self.env['hospital.patient.appointment'].create(vals)
        return {
            'type': 'ir.actions.act_window',
            'name': _('Appointment Creation'),
            'view_mode': 'form',
            'res_model': 'hospital.patient.appointment',
            'res_id': appointment_id.id,
        }
    #return view method 2 & 3
    def action_view_all_appointments(self):
        #method 1
        # action = self.env.ref('om_hospital.action_patients_appointment').read()[0]
        # action['domain'] = [('patient_id', '=', self.patient_id.id)]
        #return action
        #method 2
        #action = self.env["ir.actions.actions"]._for_xml_id("om_hospital.action_patients_appointment")
        #action['domain'] = [('patient_id', '=', self.patient_id.id)]
        #return action
        #method 3
        return {
            'type': 'ir.actions.act_window',
            'name': 'Appointment Creation',
            'view_mode': 'tree,form',
            'res_model': 'hospital.patient.appointment',
            'target': 'current',
            'domain': [('patient_id', '=', self.patient_id.id)],
        }
