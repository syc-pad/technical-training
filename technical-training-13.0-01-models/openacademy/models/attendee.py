import datetime
from dateutil import relativedelta
from odoo import api, fields, models, _

class Attendee(models.Model):
    _name = 'attendee'
    _description = 'Attendee member of the Academy'
    _order = 'id desc'
