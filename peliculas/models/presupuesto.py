# -*- coding utf-8 -*-
import logging
from odoo import   models, fields, api
from odoo.exceptions import UserError
logger = logging.getLogger(__name__)

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
    categoria_director_id = fields.Many2one('res.partner.category', string='Categoria del Director', default= lambda self: self.env['res.partner.category'].search([('name','=','Director')]))
    genero_ids = fields.Many2many('genero',string='Generos')
    vista_general = fields.Text(string='Descripcion')  
    link_trailer = fields.Char(string='Link del trailer')
    es_libro = fields.Boolean(string='Es libro', default=False)
    libro = fields.Binary(string='Libro')
    libro_filename = fields.Char(string='Nombre del libro')
    
    state = fields.Selection(selection=[('borrador','Borrador'),('aprobado','Aprobado'),('cancelado','Cancelado')], string='Estado', default='borrador', copy=False)
    fecha_aprobado = fields.Date(string='Fecha de aprobacion', copy=False)
    
    def aprobar_presupuesto(self):
        """Esta funcion cambia el estado del presupuesto a aprobado, usar el self para acceder 
            a los campos (selection) de la tabla presupuesto"""
        logger.info('============> Presupuesto Aprobado <============')
        self.state = 'aprobado'
        self.fecha_aprobado = fields.Datetime.now()
        
    
    def cancelar_presupuesto(self):
        """Esta funcion cambia el estado del presupuesto a cancelado"""
        logger.info('============> Presupuesto Cancelado <============')
        self.state = 'cancelado'
        
    def unlink(self):
        """Esta funcion permite eliminar un registro de la tabla presupuesto"""
        
        if self.state != 'cancelado':
            raise UserError('No puede eliminar un presupuesto que no este cancelado')
        super(Presupuesto, self).unlink()  
    
    @api.model
    def create(self,variables):
        logger.info(f'============> variables: {variables} <============')
        return super(Presupuesto, self).create(variables)
              
              