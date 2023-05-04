# -*- coding: utf-8 -*-
{
    'name': "Chilean states and communes",

    'summary': """
        States and communes not included in the localization
    """,

    'author': "Konos Soluciones & Servicios",
    'website': "https://www.konos.cl",

    'category': 'Localization/Chile',
    'version': '0.1',

    'depends': [
        'base_address_city',
    ],

    'data': [
        'data/res.country.state.csv',
        'data/res.city.csv',
        'views/res_company.xml',
        'views/res_partner.xml',
    ],

    'demo': [
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'GPL-3',
}
