#-*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime

class alumnos_escola(models.Model):
    _name = 'escola.alumnos'
    _description = 'escola.alumnos'

    nombre = fields.Char(string="Nombre")
    apellidos = fields.Char(string="Apellidos")
    dni = fields.Char(string="dni")
    fecha_nacimiento = fields.Date(string="Fecha de nacimiento")
    edad = fields.Integer(compute="_get_edad")
    clase = fields.Many2one('escola.clases', string="Clase", ondelete="cascade")
    eventos = fields.Many2many('escola.eventos', string="Eventos")

    @api.depends('fecha_nacimiento')
    def _get_edad(self):
        for r in self:
            if isinstance(r.fecha_nacimiento, datetime.date):
                
                any_n = r.fecha_nacimiento.year
                m_n = r.fecha_nacimiento.month
                dia_n = r.fecha_nacimiento.day
                
                any_a = datetime.datetime.now().year
                m_a = datetime.datetime.now().month
                dia_a = datetime.datetime.now().day
                
                # Utilitzem la variable -1 per a indicar que no s'ha introduit un any correcte
                
                if (any_n > any_a):
                    anys = -1
                else:
                    anys = any_a - any_n
                    if anys > 0:
                        dif_m = m_n - m_a
                        if dif_m > 0:
                            anys -= 1
                        elif dif_m == 0:
                            dif_dia = dia_n - dia_a
                            if dif_dia > 0:
                                anys -= 1
                        
                r.edad = anys
                
            else:
                r.edad = -1