import datetime
from dateutil import relativedelta
from odoo import api, fields, models, _

class Class(models.Model):
    _name = 'class'
    _description = 'Class created by a Maester'
    _order = 'id desc'
