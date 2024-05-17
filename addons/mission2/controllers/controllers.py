# -*- coding: utf-8 -*-
from odoo import http


class Mission2(http.Controller):
    @http.route('/mission2/mission2', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/mission2/mission2/objects', auth='public')
    def list(self, **kw):
        return http.request.render('mission2.listing', {
            'root': '/mission2/mission2',
            'objects': http.request.env['mission2.mission2'].search([]),
        })

    @http.route('/mission2/mission2/objects/<model("mission2.mission2"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('mission2.object', {
            'object': obj
        })

