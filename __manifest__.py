# -*- coding: utf-8 -*-
{
    'name': "Hospital Management System",

    'summary': """
        My Custom Module """,

    'description': """
        Hotel management system using Odoo.
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '1.0.0',
    'depends': ['base', 'mail'],
    'sequence': 1,

    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'application': True,
    'images': ['static/description/icon_test.png'], 



    'data': [
        'security/ir.model.access.csv',
        'views/patient_view.xml',
        'views/female_patient_view.xml',
        'views/appointment_view.xml',
        'views/menu.xml',


    ],
}
