# -*- coding: utf-8 -*-
{
    'name': "Partner sequence",

    'summary': """
        Allows you to automatically assign a partner code
    """,

    'author': "Konos Soluciones & Servicios",
    'website': "https://www.konos.cl",

    'category': 'Sales/CRM',
    'version': '0.1',

    'depends': [
        'contacts',
        'web_studio',
    ],

    'data': [
        'data/res_partner_data.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'GPL-3',
}
