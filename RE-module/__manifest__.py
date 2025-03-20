# -*- coding: utf-8 -*-
{
    'name': "Real Estate Management",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "NexFin Solutions Inc",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

{
    'name': 'Real Estate Management',
    'version': '1.0',
    'summary': 'A custom module created for testing purposes only.',
    'author': 'NF-jvillanueva',
    'email': 'jvillanueva@nexfinitsolutions.com',
    'category': 'Custom',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'views/views.xml',
        'views/templates.xml',
    ],
    'installable': True,
    'application': True,
}
