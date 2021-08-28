from odoo import models, api, fields, _

class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    _description = "doctors record"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Char(string="Name of the Doctor", required= True)
    designation  = fields.Selection([
        ('intern', 'Intern'),
        ('assistantprofessor', 'Assistant Professor'),
        ('professor', 'Professor'),
    ], string='Designation', copy=False, tracking= True )
    age = fields.Integer()
    specializaion = fields.Selection([
        ('medicine', 'Medicine'),
        ('surgery', 'Surgery'),
        ('nurology', 'Neurology'),
    ], string='specialist at ', copy=False, default= 'medicine',  tracking= True)

    def copy(self, default=None):
        if default is None:
            default = {}
        if not default.get('name'):
            default.update(name=_('%s (copy)') % (self.name))
        default['age'] = 0
        return super(HospitalDoctor, self).copy(default)