# -*- coding utf-8 -*-
from unicodedata import name
from odoo import   models, fields, api

class Presupuesto(models.Model):
    
    _name = 'presupuesto'
    _description = 'Presupuesto de peliculas para alquiler'
    
    name = fields.Char(string='Nombre', required=True)

