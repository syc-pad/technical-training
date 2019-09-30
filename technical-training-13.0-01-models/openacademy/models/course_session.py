from odoo import api, models, fields

class CourseSession(models.Model):
    _name = 'openacademy.course_session'
    _description = 'Session'

    name = fields.Char('Title')
    instructor_ids = fields.Many2many('openacademy.partner', string='Instructors', relation='session_partner_instructor_rel')
    course_id = fields.Many2one('openacademy.course', string='Course', required=True, ondelete='cascade')
    attendee_ids = fields.Many2many('openacademy.partner', string='Attendees', relation='session_partner_student_rel')
    sessiondate = fields.Datetime('Session datetime')
