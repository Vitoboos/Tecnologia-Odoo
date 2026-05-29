# -*- coding: utf-8 -*-
# from odoo import http


# class Tecnologia(http.Controller):
#     @http.route('/tecnologia/tecnologia', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tecnologia/tecnologia/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tecnologia.listing', {
#             'root': '/tecnologia/tecnologia',
#             'objects': http.request.env['tecnologia.tecnologia'].search([]),
#         })

#     @http.route('/tecnologia/tecnologia/objects/<model("tecnologia.tecnologia"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tecnologia.object', {
#             'object': obj
#         })

