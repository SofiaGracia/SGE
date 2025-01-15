#-*- coding: utf-8 -*-

from odoo import models, fields, api

class wizard_alumnos(models.TransientModel):
    
    _name = 'alumnos.wizard'
    _description = 'Wizard para marcar alumnos como activos'
    
    fecha_prova = fields.Date(string="Fecha")