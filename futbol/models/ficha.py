from odoo import   models, fields, api

class Ficha(models.Model):
    
    _name = 'ficha.jugador'
    _description = 'Clase para gestionar las fichas de los jugadores de futbol de la academia'

    # Datos personales
    name = fields.Char(string='Nombre', required=True)
    apellido = fields.Char(string='Apellidos', required=True)
    nombre_deportivo = fields.Char(string='Nombre deportivo')
    fecha_nacimiento = fields.Date(string='Fecha de nacimiento')
    dni = fields.Char(string='DNI')
    
    