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
        'views/patient.xml',
        'views/sales.xml',
        'views/doctor.xml',

    ],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
