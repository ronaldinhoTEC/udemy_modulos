# -*- coding utf-8 -*-
from odoo import   models, fields, api

class Presupuesto(models.Model):
    
    _name = 'presupuesto'
    _description = 'Presupuesto de peliculas para alquiler'
    
    name = fields.Char(string='Nombreee', required=True)
    clasificacion = fields.Selection(selection=[('g','Publico General'),('PG','Mayores de 18 años'),('PG-13','Mayores de 13 años'),('R','Mayores de 17 años'),('NC-17','Mayores de 18 años'),('R','Se recomienda la compañia de un adulto')])
    fecha_estreno = fields.Date(string='Fecha de estreno')
    punctuacion = fields.Float(string='Puntuacion', digits=(2,1))
    active = fields.Boolean(string='Activo', default=True)