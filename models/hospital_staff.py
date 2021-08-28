from odoo import fields, models, api , _


class HospitalStaff(models.Model):
    _name = "hospital.staff"
    _description = "Hospital staff details"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="name of Employee", required = True )
    age = fields.Integer(string="age")
    dept = fields.Selection([
        ('pathology','Pathology'),
        ('cleaning','Cleaning'),
        ('management','Management'),
        ('inventory','Inventory'),
        ('hr', 'HR')
    ], tracking = True , required = True , default = 'management')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string='Gender', required=True, copy=False, default='male', tracking=True)
    join_date = fields.Date(string="join date")
    salary = fields.Integer(string="Salary")
    image = fields.Binary(string="Patient image")
