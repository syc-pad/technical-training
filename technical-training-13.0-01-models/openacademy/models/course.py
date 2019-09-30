from odoo import api, models, fields

# Correction
COURSE_LEVEL = [
    ('0', 'All'),
    ('1', 'Beginner'),
    ('2', 'Intermediate'),
    ('3', 'Expert'),
]

class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'Course'

    name = fields.Char('Title')
    description = fields.Text('Description')
    session_ids = fields.One2many('openacademy.session', 'course_id')
    level = fields.Selection(COURSE_LEVEL, string='Level', default='0')
