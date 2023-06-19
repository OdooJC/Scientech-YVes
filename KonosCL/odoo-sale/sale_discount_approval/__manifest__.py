# -*- coding: utf-8 -*-
{
    'name': "Sale Discount Approval",

    'summary': """
        Managers must approve discounts granted on sales order lines.
    """,

    'author': "Konos Soluciones & Servicios",
    'website': "https://www.konos.cl",

    'category': 'Sales',
    'version': '0.1',

    'depends': [
        'sale_order_approval',
    ],

    'data': [
        'views/res_config_settings_views.xml',
    ],

    'demo': [
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
}
