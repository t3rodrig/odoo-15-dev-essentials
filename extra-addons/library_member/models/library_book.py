# -*- coding: utf-8 -*-

from odoo import models, fields


class Book(models.Model):
    _inherit = "library.book"
    is_available = fields.Boolean("Is Available?")
