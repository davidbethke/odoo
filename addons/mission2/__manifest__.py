# -*- coding: utf-8 -*-
{
    'name': "mission2",

    'summary': "Mission to fly, pre, post, flight plans, status",

    'description': """
customer assigned and payed
pilot assigned, payout and incentives
status of mission
pre, post, in-flight plan

    """,

    'author': "Residence Drone",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Human Resources/Employees',
    'version': '0.4',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}

