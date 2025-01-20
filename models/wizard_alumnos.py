#-*- coding: utf-8 -*-

from odoo import models, fields, api

class wizard_alumnos(models.TransientModel):
    
    _name = 'alumnos.wizard'
    _description = 'Wizard para marcar alumnos como activos'
    
    # Nos tiene que permitir marcar a los alumnos como activos
    alumnos_activos = fields.Many2one('escola.alumnos', string='Alumnos',required=True,domain=[('active','=',False)])
    
    def marcar_activos(self):
        """
        Aquesta funció actualitza l'estat dels alumnes seleccionats a 'active'.
        """
        for alumno in self.alumnos_activos:
            alumno.active = True