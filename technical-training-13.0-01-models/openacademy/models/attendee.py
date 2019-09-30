import datetime
from dateutil import relativedelta
from odoo import api, fields, models, _

class Attendee(models.Model):
    _name = 'attendee'
    _description = 'Attendee member of the Academy'
    _order = 'id desc'

    firstname = fields.Char(required=True)
    lastname = fields.Char(required=True)

    # Class (pour savoir dans quelle classe il est inscrit)
