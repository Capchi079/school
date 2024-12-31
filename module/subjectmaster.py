from odoo import models, fields, api
class SubjectMaster(models.Model):
    _name = 'subject.master'
    _description = 'Subject Master'

    # name = fields.Char(string='Subject Name', required=True)
    # subject_code = fields.Char(string='Subject Code', required=True, copy=False, readonly=True, default=lambda self: self.env['ir.sequence'].next_by_code('subject.master.code'))
    name = fields.Char(string='Subject Name', required=True)
    subject_code = fields.Char(string='Subject Code', required=True, unique=True, default=lambda self: self.env['ir.sequence'].next_by_code('subject.master.code'),readonly=True)
    class_level = fields.Selection([
        ('1', '1st'),
        ('2', '2nd'),
        ('3', '3rd'),
        ('4', '4th'),
        ('5', '5th'),
        ('6', '6th'),
        ('7', '7th'),
        ('8', '8th'),
        ('9', '9th'),
        ('10', '10th'),
        ('GRADUATE', 'B>TECH'),
    ], string="Class", required=True)
    exam_marks_line_ids = fields.One2many('exam.marks.line', 'subject_id')
    marks = fields.Integer(string='Total Marks', required=True)
    # @api.model
    # def create(self, vals):
    #     # if vals.get('subject_code', _('New')) == _('New'):
    #     #     vals['subject_code'] = self.env['ir.sequence'].next_by_code('subject.master') or _('New')
    #     vals= {
    #         'name': 'History',
    #         'class_level': '10',
    #         'marks': '300'}
    #     return super(SubjectMaster, self).create(vals)




