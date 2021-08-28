# -*- coding: utf-8 -*-
{
    'name': 'Hospital Management',
    'version': '1.0',
    'summary': 'Hospital Management Software',
    'sequence': -100,
    'description': """Hospital management software for xyz hospital""",
    'category': 'Productivity',
    'depends': ['sale'],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'wizard/create_appointment_view.xml',
        'wizard/search_appointment.xml',
        'views/patient.xml',
        'views/hospital_staff_view.xml',
        'views/sales.xml',
        'views/doctor.xml',
        'views/kids_view.xml',
        'views/patient_gender_view.xml',
        'views/appoinment_view.xml'

    ],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
