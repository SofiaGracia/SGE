#-*- coding: utf-8 -*-

from odoo import models, fields, api

class clases_escola(models.Model):
    _name = 'escola.clases'
    _description = 'escola.clases'

    active = fields.Boolean(string="Activo", default=True)
    curso = fields.Char(string="Curso", required=True, help="Introduce el curso")
    nivel = fields.Selection([('0','1'), ( '1','2')], string="Nivel", default="0")
    fecha_inicio = fields.Date(string="Fecha inicio")
    fecha_final = fields.Date(string="Fecha final")
    tutor = fields.Many2one('hr.employee', string="Profesor", ondelete="cascade",domain=[('es_professor','=',True)])
    #Numero de alumnos (calculado)
    alumnos = fields.One2many(comodel_name='escola.alumnos', inverse_name='clase',string="Alumnos de la clase")
    total_alumnos = fields.Integer(string="Total de alumnos",compute="_compute_alumnos")
    descripcion = fields.Char(string="Descripción", required=True, help="Introduce una descripción")
    
    
    @api.depends('alumnos')
    def _compute_alumnos(self):
        for r in self:
            r.total_alumnos = len(r.alumnos)