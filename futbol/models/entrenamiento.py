from odoo import   models, fields, api

class EntrenamientoEntrenamiento(models.Model):
    
    _name = 'entrenamiento.entrenamiento'
    _description = 'Clase para gestionar los entrenamientos de los jugadores de futbol de la academia'
    
    name = fields.Char(string='Nombre', required=True)
    ejercicio = fields.Char(string='Ejercicio', required=True)
    ejercicio2 = fields.Char(string='Ejercicio', required=True)

