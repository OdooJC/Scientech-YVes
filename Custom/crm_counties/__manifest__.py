# -*- coding: utf-8 -*-
{
    'name': "CRM Counties",

    'summary': """
        Enables the states and communes for leads
    """,

    'author': "Konos Soluciones & Servicios",
    'website': "https://www.konos.cl",

    'category': 'Sales/CRM',
    'version': '0.1',

    'depends': [
        'crm',
        'l10n_cl_counties',
    ],

    'data': [
        'views/crm_lead_views.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'GPL-3',
}
