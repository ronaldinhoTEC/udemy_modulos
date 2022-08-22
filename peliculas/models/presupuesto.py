# -*- coding utf-8 -*-
from locale import currency
import logging
from signal import default_int_handler
from odoo import   models, fields, api
from odoo.exceptions import UserError
logger = logging.getLogger(__name__)

class Presupuesto(models.Model):
    
    _name = 'presupuesto'
    _description = 'Presupuesto de peliculas para alquiler'
    _inherit = ['mail.thread','mail.activity.mixin','image.mixin']
    
    @api.depends('detalle_ids')
    def _compute_total(self):
        for record in self:
            sub_total = 0
            for linea in record.detalle_ids:
                sub_total += linea.importe
            record.base = sub_total
            record.impuestos = sub_total * 0.18
            record.total = sub_total + record.impuestos
            
    foto = fields.Binary(string="Foto")
    name = fields.Char(string='Pelicula', required=True)
    clasificacion = fields.Selection(selection=[('g','Publico General'),('PG','Mayores de 18 años'),('PG-13','Mayores de 13 años'),('R','Mayores de 17 años'),('NC-17','Mayores de 18 años'),('R','Se recomienda la compañia de un adulto')])
    dsc_clasificacion = fields.Char(string='Descripcion de la clasificacion', compute='_onchange_clasificacion')
    fecha_estreno = fields.Date(string='Fecha de estreno')
    puntuacion = fields.Float(string='Puntuacion', related='puntuacion2') # related: Campo para copiar un valor de otro campo de otra tabla (en este caso de la tabla puntuacion2)
    puntuacion2 = fields.Float(string='Puntuacion')
    active = fields.Boolean(string='Activo', default=True)
    # apellido = fields.Char(string='Apellido', required=True)
    director_id = fields.Many2one('res.partner', string='Director', required=True)
    # VERSION1 :categoria_director_id = fields.Many2one('res.partner.category', string='Categoria del Director', default= lambda self: self.env['res.partner.category'].search([('name','=','Director')]))
    categoria_director_id = fields.Many2one('res.partner.category', string='Categoria del Director', default= lambda self: self.env.ref('peliculas.category_director'))
    categoria_actor_id = fields.Many2one('res.partner.category', string='Categoria del Actor', default= lambda self: self.env.ref('peliculas.category_actor'))
    
    genero_ids = fields.Many2many('genero',string='Generos')
    vista_general = fields.Text(string='Descripcion')  
    link_trailer = fields.Char(string='Link del trailer')
    es_libro = fields.Boolean(string='Es libro', default=False)
    libro = fields.Binary(string='Libro')
    libro_filename = fields.Char(string='Nombre del libro')
    
    state = fields.Selection(selection=[('borrador','Borrador'),('aprobado','Aprobado'),('cancelado','Cancelado')], string='Estado', default='borrador', copy=False)
    fecha_aprobado = fields.Date(string='Fecha de aprobacion', copy=False)
    num_presupuesto = fields.Char(string='Numero de presupuesto', copy=False)
    fecha_creacion = fields.Datetime(string='Fecha de creacion',copy=False, default= lambda self: fields.Datetime.now())
    # actores
    actor_ids = fields.Many2many('res.partner', string='Actores')
    opinion = fields.Html(string='Opinion')
    detalle_ids = fields.One2many('presupuesto.detalle', inverse_name='presupuesto_id', string='Detalle del presupuesto')
    campos_ocultos = fields.Boolean(string='Campos ocultos', default=False)
    currency_id = fields.Many2one('res.currency', string='Moneda', default= lambda self: self.env.company.currency_id.id)
    terminos = fields.Text(string='Terminos y condiciones')
    base = fields.Monetary(string='Base imponible', compute='_compute_total')
    impuestos = fields.Monetary(string='Impuesto', compute='_compute_total')
    total = fields.Monetary(string='Total', compute='_compute_total')
    
    # test
    # serie = fields.Char(string='Serie', related='')
    
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
        for record in self:
            if record.state != 'cancelado':
                raise UserError('No puede eliminar un presupuesto que no este cancelado')
            super(Presupuesto, record).unlink()
          
    
    @api.model
    def create(self,variables):
        logger.info(f'============> variables: {variables} <============')
        sequence_obj = self.env['ir.sequence']
        correlativo = sequence_obj.next_by_code('secuencia.presupuesto.pelicula')
        variables['num_presupuesto'] = correlativo
        return super(Presupuesto, self).create(variables)
    
    def write(self,variables):
        logger.info(f'============> variables editadas: {variables} <============')
        if 'clasificacion' in variables:
            raise UserError('No puede cambiar la clasificacion de la pelicula')
            
        return super(Presupuesto, self).write(variables)
    
    def copy(self, default=None):
        default = dict(default or {})
        default['name'] = self.name + ' (Copiaa)'
        
        return super(Presupuesto, self).copy(default)


    @api.onchange('clasificacion')
        # Em este decorador se puede agregar mas campos para que se actualicen cuando se cambie el valor de clasificacion	
    def _onchange_clasificacion(self):
        if self.clasificacion:
            if self.clasificacion == 'g':
                self.dsc_clasificacion = 'Publico General'
            
            if self.clasificacion == 'PG':
                self.dsc_clasificacion = 'Mayores de 18 años'
            
            if self.clasificacion == 'PG-13':
                self.dsc_clasificacion = 'Mayores de 13 años'
            
            if self.clasificacion == 'R':
                self.dsc_clasificacion = 'Mayores de 17 años'
                
            if self.clasificacion == 'NC-17':
                self.dsc_clasificacion = 'Mayores de 18 años'
                
        else:
            self.dsc_clasificacion = False
                
class PresupuestoDetalle(models.Model):
    
    _name = 'presupuesto.detalle'
    _description = ''

    presupuesto_id = fields.Many2one('presupuesto', string='Presupuesto')
    name = fields.Many2one('recurso.cinematografico', string='Recurso')
    descripcion = fields.Char(string='Descripcion', related='name.descripcion')
    contacto_id = fields.Many2one('res.partner', string='Contacto', related='name.contacto_id')             
    imagen = fields.Binary(string='Imagen', related='name.imagen')
    cantidad = fields.Float(string='Cantidad',default="1",digit=(16,4))
    precio = fields.Float(string='Precio',digit="Product Price")  
    importe = fields.Monetary(string='Importe')    
    
    currency_id = fields.Many2one('res.currency', string='Moneda'
                                    ,related='presupuesto_id.currency_id')
    
    @api.onchange('name')
    def _onchange_name(self):
        if self.name:
            self.precio = self.name.precio
            
    @api.onchange('cantidad','precio')
    def _onchange_importe(self):
        if self.cantidad and self.precio:
            self.importe = self.cantidad * self.precio
                