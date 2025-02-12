# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json


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

    @http.route('/mission2/mission2/objects/description/<model("mission2.mission2"):obj>', auth='public')
    def description(self, obj, **kw):
        return http.request.render('mission2.description', {
            'object': obj
        })

    @http.route('/mission2/mission2/list', type='json', auth="user")
    def listJSON(self, **kw):
        #missions = request.env['mission2.mission2'].sudo().search([])
        missions = request.env['mission2.mission2'].search([])
        resp = {}
        allresp=[]
        for mission in missions:
            resp[mission.name]= mission.value
            allresp.append(resp.copy())
            resp.clear()
        output = {
        'results':{
            'code':200,
            'message':'OK'
             }
        }
        return json.dumps(allresp)
        #return http.Response(json.dumps(output), status=200, headers={"Content-type": "application/json"})

    @http.route('/mission2/request/list', type='json', auth="user")
    def listJSON(self, **kw):
        requests = request.env['mission2.request'].search([])
        resp = {}
        allresp=[]
        for request in requests:
            resp[request.name]= request.value
            allresp.append(resp.copy())
            resp.clear()
        return json.dumps(allresp)

    @http.route('/mission2/auction/list', type='json', auth="user")
    def listJSON(self, **kw):
        auctions = request.env['mission2.auction'].search([])
        resp = {}
        allresp=[]
        for auction in auctions:
            resp[auction.name]= auction.value
            allresp.append(resp.copy())
            resp.clear()
        return json.dumps(allresp)

    @http.route('/mission2/report/list', type='json', auth="user")
    def listJSON(self, **kw):
        reports = request.env['mission2.report'].search([])
        resp = {}
        allresp=[]
        for report in reports:
            resp[report.name]= report.value
            allresp.append(resp.copy())
            resp.clear()
        return json.dumps(allresp)




