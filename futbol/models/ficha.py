from odoo import   models, fields, api

class Ficha(models.Model):
    
    _name = 'ficha.jugador'
    _description = 'Clase para gestionar las fichas de los jugadores de futbol de la academia'

    # Datos personales
    name = fields.Char(string='Nombre', required=True)
    apellido = fields.Char(string='Apellidos', required=True)
    nombre_deportivo = fields.Char(string='Nombre deportivo')
    fecha_nacimiento = fields.Date(string='Fecha de nacimiento')
    edad = fields.Integer(string='Edad')
    dni = fields.Char(string='DNI')
    # datos de contacto
    celular = fields.Char(string='Celular')
    email = fields.Char(string='Email')
    # datos deportivos
    posicion = fields.Selection(selection=[('arquero','Arquero'),('defensa','Defensa'),('centrocampista','Centrocampista'),('delantero','Delantero')])
    dorsal = fields.Integer(string='Dorsal')
    equipo_simpatizante = fields.Many2one('equipo.equipo', string='Equipo simpatizante')
    # datos de la familia
    name_padre = fields.Char(string='Nombre del padre')
    telefono_padre = fields.Char(string='Telefono del padre')
    