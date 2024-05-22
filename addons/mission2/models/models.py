# -*- coding: utf-8 -*-

from odoo import models, fields, api


class mission2(models.Model):
     _name = 'mission2.mission2'
     _description = 'mission2.mission2'

     name = fields.Char()
     value = fields.Integer()
     value2 = fields.Float(compute="_value_pc", store=True)
     description = fields.Text()
     flightplan = fields.One2many('mission2.flightplan', 'fp')
     status = fields.Many2one('mission2.flightplan')

     @api.depends('value')
     def _value_pc(self):
         for record in self:
             record.value2 = float(record.value) / 100

