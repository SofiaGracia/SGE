#-*- coding: utf-8 -*-

from odoo import models, fields, api

class eventos_escola(models.Model):
    _name = 'escola.eventos'
    _description = 'escola.eventos'


    tipo = fields.Selection([('0','Ausencia'), ( '1','Retraso'), ('2','Felicitación'), ('3','Comportamiento')], string="Seleccion", default="0")
    fecha = fields.Date(string="Data d'Inici")
    descripcion = fields.Char(string="Descripción", required=True, help="Introduce la descripción del evento")
    
    
    # Si és Many2many i sols vore-ho en esta pantalla (eventos) no fa falta definir-ho en les altres classes
    # Relación con clase
    clase = fields.Many2many('escola.clases', string="Clases")
    # Relación con profesor
    # profesor = fields.Many2many('escola.profesors', string="Professors")
    # Relación con alumno
    alumno = fields.Many2many('escola.alumnos', string="Alumnos")
