from odoo import api, models, fields

class Partner(models.Model):
    _name = 'openacademy.partner'
    _description = 'Partner'

    name = fields.Char('Name')
    type = fields.Selection([('student','Student'), ('teacher', 'Teacher')], default='student')
    comment = fields.Char(compute='_compute_comment')

@api.depends('name')
def _compute_comment(self):
    if record.name == "Pouic Pouic":
        self.comment = "Quel nom ridicule !""
