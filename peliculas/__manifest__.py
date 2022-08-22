# -*- coding utf-8 -*-
{
    'name': 'Peliculas',
    'version': '1.0',
    'depends': ['base','contacts','mail','base_setup', 'board','account'],
    'author': 'Ronaldinho Farfan',
    'category': 'Peliculas',
    'description': """Este modulo le permite gestionar las peliculas que se alquilan en la tienda de videos de Ronaldinho Farfan""",
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/secuencia.xml',
        'data/categoria.xml',
        'wizard/update_wizard_views.xml',
        'views/presupuesto_views.xml',
        'report/reporte_peliculas.xml',
        'views/menu.xml',
    ]
}