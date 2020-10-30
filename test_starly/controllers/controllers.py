# -*- coding: utf-8 -*-
# from odoo import http


# class TestStarly(http.Controller):
#     @http.route('/test_starly/test_starly/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/test_starly/test_starly/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('test_starly.listing', {
#             'root': '/test_starly/test_starly',
#             'objects': http.request.env['test_starly.test_starly'].search([]),
#         })

#     @http.route('/test_starly/test_starly/objects/<model("test_starly.test_starly"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('test_starly.object', {
#             'object': obj
#         })
