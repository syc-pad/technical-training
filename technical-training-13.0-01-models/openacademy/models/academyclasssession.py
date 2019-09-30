import datetime
from dateutil import relativedelta
from odoo import api, fields, models, _

class Academyclasssession(models.Model):
    _name = 'academyclasssession'
    _description = 'Session of an Academyclass'
    _order = 'sessiondate asc, name asc'

    name = fields.Char(required=True)
    sessiondate = fields.Datetime('Session datetime')
    course_id = fields.Many2one('academyclass', string='Cours', required=True, ondelete='cascade')
    # masterclass = fields.One2many('academyclass')
