from odoo import models, api, fields

class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    _description = "doctors record"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Char(string="Name of the Doctor", required= True)
    designation  = fields.Selection([
        ('intern', 'Intern'),
        ('assistantprofessor', 'Assistant Professor'),
        ('professor', 'Professor'),
    ], string='Designation',  required=True, copy=False, default= 'intern', tracking= True)
    age = fields.Integer()
    specializaion = fields.Selection([
        ('medicine', 'Medicine'),
        ('surgery', 'Surgery'),
        ('nurology', 'Neurology'),
    ], string='specialist at ',  required=True, copy=False, default= 'medicine', tracking= True)

