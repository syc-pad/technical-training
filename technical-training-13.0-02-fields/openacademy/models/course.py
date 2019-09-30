# -*- coding: utf-8 -*-
import logging
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)

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
    total_attendees = fields.Integer(compute='_compute_attendies', store=True)

    instructor_id = fields.Many2one('openacademy.partner', string="Instructor")
    level = fields.Selection(related='course_id.level')
    course_id = fields.Many2one('openacademy.course', ondelete='cascade', string="Course", required=True)
    attendee_ids = fields.Many2many('openacademy.partner', string="Attendees")

    # Pour les depends, le live reload fait le boulot
    @api.depends('attendee_ids')
    def _compute_attendies(self):
        for record in self:
            record.total_attendees = len(record.attendee_ids)

    # Pour les onChange, il faut faire F5
    @api.onchange('total_attendees', 'maximum_capacity')
    def check_capacity(self):
        #for record in self: (inutile pour un onchange)
        if (self.maximum_capacity < len(self.attendee_ids)):
            self.attendance_state = 'over'
        if (self.maximum_capacity > len(self.attendee_ids)):
            self.attendance_state = 'under'
        if (self.maximum_capacity == len(self.attendee_ids)):
            self.attendance_state = 'ok'

    @api.constrains('attendee_ids')
    def check_instructor_not_attendee(self):
        for record in self:
            if record.instructor_id in record.attendee_ids:
                _logger.info('ID du prof %s', record.instructor_id)
                raise ValidationError("Le professeur %s ne peut pas être participant" % record.instructor_id.name)

    @api.constrains('start_date')
    def check_date(self):
        # Date.today() ou Datetime.now()
        if self.start_date < fields.Date.today():
            raise ValidationError(_('Le cours ne peut avoir lieu dans le passé'))
