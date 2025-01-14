#-*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime

class eventos_escola(models.Model):
    _name = 'escola.eventos'
    _description = 'escola.eventos'

    #Hem de posar-li un nom a l'event
    #nombre = fields.Char(string="Nombre del evento", compute="_compute_nom")

    # Esta funció tamb pot ser una lambda
    #def _obtindre_data(self):
    #    return datetime.datetime.now()

    tipo = fields.Selection([('0','Ausencia'), ( '1','Retraso'), ('2','Felicitación'), ('3','Comportamiento')], string="Seleccion", default="0")
    # Si volguerem mostrar també l'hora deuria de ser de tipus Datetime
    fecha = fields.Date(string="Data d'Inici",default=lambda d: datetime.datetime.now())
    descripcion = fields.Char(string="Descripción", required=True, help="Introduce la descripción del evento")
    
    
    # Si és Many2many i sols vore-ho en esta pantalla (eventos) no fa falta definir-ho en les altres classes
    # Relación con clase
    clase = fields.Many2many('escola.clases', string="Clases")
    # Relación con profesor
    # profesor = fields.Many2many('escola.profesors', string="Professors")
    # Relación con alumno
    alumno = fields.Many2many('escola.alumnos', string="Alumnos")