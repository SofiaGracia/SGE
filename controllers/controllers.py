# -*- coding: utf-8 -*-
# from odoo import http


# class GestioEscola(http.Controller):
#     @http.route('/gestio_escola/gestio_escola', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestio_escola/gestio_escola/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestio_escola.listing', {
#             'root': '/gestio_escola/gestio_escola',
#             'objects': http.request.env['gestio_escola.gestio_escola'].search([]),
#         })

#     @http.route('/gestio_escola/gestio_escola/objects/<model("gestio_escola.gestio_escola"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestio_escola.object', {
#             'object': obj
#         })
