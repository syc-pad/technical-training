import datetime
from dateutil import relativedelta
from odoo import api, fields, models, _
from . import maester

ACADEMYCLASS_LEVEL = [
    ('0', 'All'),
    ('1', 'Beginner'),
    ('2', 'Intermediate'),
    ('3', 'Expert'),
]

class Academyclass(models.Model):
    _name = 'academyclass'
    _description = 'Class created by a Maester'
    _order = 'id desc'

    name = fields.Char(required=True, string='Nom du cours')
    level = fields.Selection(ACADEMYCLASS_LEVEL, string='Level', default='0')
    maester_id = fields.Many2one('maester', string='Maester')
    students = fields.Many2many('attendee')
