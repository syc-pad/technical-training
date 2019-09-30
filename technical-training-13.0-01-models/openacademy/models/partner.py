from odoo import api, models, fields

class Partner(models.Model):
    _name = 'openacademy.partner'
    _description = 'Partner'

    name = fields.Char('Name')
    type = fields.Selection([('student','Student'), ('teacher', 'Teacher')], default='student')
