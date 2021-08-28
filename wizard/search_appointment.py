from odoo import api, fields, models, _


class SearchAppointment(models.TransientModel):
    _name = "search.appointment.wizard"
    _description = "search appointment"

    patient_id = fields.Many2one('hospital.patient', string="patient", required= True)

    def appointment_search_m1(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Appointment Creation',
            'view_mode': 'tree,form',
            'res_model': 'hospital.patient.appointment',
            'target': 'current',
            'domain': [('patient_id', '=', self.patient_id.id)],
        }

