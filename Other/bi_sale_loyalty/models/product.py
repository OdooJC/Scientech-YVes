# -*- coding: utf-8 -*-

from itertools import groupby
from datetime import datetime, timedelta

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_is_zero, float_compare, DEFAULT_SERVER_DATETIME_FORMAT
from odoo.tools.misc import formatLang
from odoo.tools import html2plaintext
import odoo.addons.decimal_precision as dp

class InheritProduct(models.Model):
	
	_inherit = "product.template"

	num_of_points = fields.Integer("Number of Points")
	is_gift_product = fields.Boolean("Gift Product")
	is_commissionable = fields.Boolean(default="True")
