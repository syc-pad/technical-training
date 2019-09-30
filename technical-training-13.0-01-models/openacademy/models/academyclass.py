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

    coursename = fields.Char(required=True)
    level = fields.Selection(ACADEMYCLASS_LEVEL, string='Level', default='0')
    responsible = fields.One2many('maester', inverse_name='maester_id')
