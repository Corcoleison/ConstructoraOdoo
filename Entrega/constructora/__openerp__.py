# -*- coding: utf-8 -*-
{
    'name': "Constructora",

    'summary': """
        Este modulo de Odoo esta destinado a empresas constructoras que realicen varios servicios de construccion y reformas""",

    'description': """
        Este modulo de Odoo esta destinado a empresas constructoras que realicen varios servicios de construccion y reformas
    """,

    'author': "Pablo Corcoles Molina",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
	'views/constructora.xml',
        'views/partner.xml',
        'reports.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
