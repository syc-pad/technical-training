import datetime
from dateutil import relativedelta
from odoo import api, fields, models, _

class Academyclass(models.Model):
    _name = 'academyclass'
    _description = 'Class created by a Maester'
    _order = 'id desc'
