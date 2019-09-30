import datetime
from dateutil import relativedelta
from odoo import api, fields, models, _

class Academyclasssession(models.Model):
    _name = 'academyclasssession'
    _description = 'Session of an Academyclass'
    _order = 'sessiondate asc, name asc'

    name = fields.Char(required=True)
    sessiondate = fieds.Datetime('Session datetime')
    masterclass = fields.One2many('academyclass')
