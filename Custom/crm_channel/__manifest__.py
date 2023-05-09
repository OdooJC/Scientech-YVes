# -*- coding: utf-8 -*-
{
    'name': "CRM Sale Channel",

    'summary': """
        Enables sales channels on leads and opportunities
    """,

    'author': "Konos Soluciones & Servicios",
    'website': "https://www.konos.cl",

    'category': 'Sales/CRM',
    'version': '0.1',

    'depends': [
        'crm',
        'sale_channel',
    ],

    'data': [
        'views/crm_lead_views.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'GPL-3',
}
