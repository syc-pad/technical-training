import datetime
from dateutil import relativedelta
from odoo import api, fields, models, _

class Maester(models.Model):
    _name = 'maester'
    _description = 'Maester giving courses in the Academy'
    _order = 'id desc'

    firstname = fields.Char(required=True)
    lastname = fields.Char(required=True)
    
