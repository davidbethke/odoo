
from odoo import models, fields


class status(models.Model):
     _name = 'mission2.status'
     _description = 'mission2.status'

     name = fields.Char()
     status = fields.Integer()
     description = fields.Text()