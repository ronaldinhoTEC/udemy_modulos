from odoo import   models, fields, api

class RecursoCinematografico(models.Model):
    
    _name = 'recurso.cinematografico'
    _description = ''

    name = fields.Char(string='Recurso', required=True)
    descripcion = fields.Char(string='Descripcion')
    precio = fields.Float(string='Precio')
    contacto_id = fields.Many2one('res.partner',domain="[('is_company','=',False)]",string='Contacto')
    imagen = fields.Binary(string='Imagen')
    