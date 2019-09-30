import datetime
from dateutil import relativedelta
from odoo import api, fields, models, _

class Attendee(models.Model):
    _name = 'attendee'
    _description = 'Attendee member of the Academy'
    _order = 'id desc'
    # inherit('res.partner') pour qu'il hérite carrément de res.partner

    firstname = fields.Char(required=True)
    lastname = fields.Char(required=True)
    attendeeclass = fields.Many2many('academyclass')

# def name_get() pour override le comportement du display_name
