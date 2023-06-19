# -*- coding: utf-8 -*-
{
    'name': "Sale Order Approval",

    'summary': """
        Managers must approve sales orders depending on the partner credit
        limit
    """,

    'author': "Konos Soluciones & Servicios",
    'website': "https://www.konos.cl",

    'category': 'Sales',
    'version': '0.2',

    'depends': [
        'sale_management',
        'account_followup',
    ],

    'data': [
        'data/res_groups.xml',
        'data/mail_template.xml',
        'views/res_partner_views.xml',
        'views/sale_order_views.xml',
    ],

    'demo': [
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
}
