from odoo import   models, fields, api

class Principal(models.Model):
    
    _name = 'principal'
    _description = 'Esta clase es la vista principal del modulo de futbol'
    
    # Datos principales
    name = fields.Char(string='Nombre', required=True)
    director_tecnico = fields.Many2one('res.partner', string='Director Tecnico', required=True)


