#-*- coding: utf-8 -*-

from odoo import models, fields, api

class profesors_escola(models.Model):
    
    _inherit = 'hr.employee'
    
    
    # Professor hereta de res partner i es vora en una pestanya que tindrà un camp isTeacher que es Boolean
    # i un camp classes que serà una llista
    es_professor = fields.Boolean(string="Es profesor")
    clase = fields.One2many('escola.clases', 'tutor', string="Clases del tutor")
