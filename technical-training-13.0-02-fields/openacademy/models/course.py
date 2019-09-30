# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'Course'

    name = fields.Char(string='Title', required=True)
    description = fields.Text()

    responsible_id = fields.Many2one('openacademy.partner', string="Responsible")
    session_ids = fields.One2many('openacademy.session', 'course_id', string="Sessions")

    level = fields.Selection([('1', 'Easy'), ('2', 'Medium'), ('3', 'Hard')], string="Difficulty Level")


class Session(models.Model):
    _name = 'openacademy.session'
    _description = 'Session'

    name = fields.Char(required=True)
    active = fields.Boolean(default=True)
    state = fields.Selection([('draft', "Draft"), ('confirmed', "Confirmed"), ('done', "Done")], default='draft')
    attendance_state = fields.Selection([('ok', "OK"), ('under', "Sous-remplie"), ('over', "Over-bookée")], default='ok')

    start_date = fields.Date(default=fields.Date.context_today)
    duration = fields.Float(digits=(6, 2), help="Duration in days", default=1)
    maximum_capacity = fields.Integer(string="Capacité d'accueil", default=10)
    total_attendees = fields.Float(compute='_compute_attendies', store=True)

    instructor_id = fields.Many2one('openacademy.partner', string="Instructor")
    course_id = fields.Many2one('openacademy.course', ondelete='cascade', string="Course", required=True)
    attendee_ids = fields.Many2many('openacademy.partner', string="Attendees")

@api.depends('attendee_ids')
def _compute_attendies(self):
    for record in self:
        record.total_attendees = len(record.attendee_ids)

@api.onchange('total_attendees')
def check_capacity(self):
    if (self.maximum_capacity > len(record.attendee_ids)):
        self.attendance_state = 'over'
    if (self.maximum_capacity < len(record.attendee_ids)):
        self.attendance_state = 'under'
    if (self.maximum_capacity == len(record.attendee_ids)):
        self.attendance_state = 'ok'
