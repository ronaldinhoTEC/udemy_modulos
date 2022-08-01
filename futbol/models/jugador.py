from odoo import   models, fields, api

class Entrenamiento(models.Model):
    
    _name = 'jugador.entrenamiento'
    _description = 'entramiento del jugador'

    name = fields.Char(string='Nombre', required=True)
    entrenamiento = fields.Many2one('entrenamiento.entrenamiento', string='Entrenamiento', required=True)
    fecha_entre = fields.Date(string='Fecha', required=True)
    profesor = fields.Many2one('res.partner', string='Profesor', required=True)