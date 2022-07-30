# -*- coding utf-8 -*-
import string
from odoo import   models, fields, api

class Presupuesto(models.Model):
    
    _name = 'presupuesto'
    _description = 'Presupuesto de peliculas para alquiler'
    _inherit = ['image.mixin']
    
    
    foto = fields.Binary(string="Foto")
    name = fields.Char(string='Pelicula', required=True)
    clasificacion = fields.Selection(selection=[('g','Publico General'),('PG','Mayores de 18 años'),('PG-13','Mayores de 13 años'),('R','Mayores de 17 años'),('NC-17','Mayores de 18 años'),('R','Se recomienda la compañia de un adulto')])
    fecha_estreno = fields.Date(string='Fecha de estreno')
    puntuacion = fields.Float(string='Puntuacion', related='puntuacion2') # related: Campo para copiar un valor de otro campo de otra tabla (en este caso de la tabla puntuacion2)
    puntuacion2 = fields.Float(string='Puntuacion')
    active = fields.Boolean(string='Activo', default=True)
    # apellido = fields.Char(string='Apellido', required=True)
    director_id = fields.Many2one('res.partner', string='Director', required=True)
    genero_ids = fields.Many2many('genero',string='Generos')
    vista_general = fields.Text(string='Descripcion')  
    link_trailer = fields.Char(string='Link del trailer')
    es_libro = fields.Boolean(string='Es libro', default=False)
    libro = fields.Binary(string='Libro')
    libro_filename = fields.Char(string='Nombre del libro')
    
      