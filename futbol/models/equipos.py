from odoo import   models, fields, api

class Equipo(models.Model):
    
    _name = 'equipo.equipo'
    _description = 'Clase de equipos de futbol'

    # Datos del equipo
    name = fields.Char(string='Nombre', required=True)
    pais = fields.Char(string='Pais')
    ciudad = fields.Char(string='Ciudad')
    director_tecnico = fields.Many2one('res.partner', string='Director Tecnico', required=True)

