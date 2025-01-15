# -*- coding: utf-8 -*-
{
    'name': "escola",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr'],

    # always loaded
    # L'ordre en el manifest es important
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/eventos.xml',
        'views/profesores.xml',
        'views/clases.xml',
        'views/wizard_alumnos.xml',
        'views/alumnos.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
