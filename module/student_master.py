# # from datetime import date
# #
# # from docutils.nodes import address
# # from pkg_resources import require
# #
# # from odoo import api, fields, models
# # from odoo.tools.populate import compute
# #
# #
# #
# # class StudentMaster(models.Model):
# #     _name = 'student.master'
# #     _description = 'details about the student master'
# #
# #     name=fields.Char(string='Name', reqired=True)
# #     student_code = fields.Char(string='Student Code', readonly=True, copy=False)
# #     age=fields.Integer(string='Age', compute='_compute_age')
# #     address=fields.Char(string='address')
# #     DOB=fields.Date(string='Date_of_birth', reqired=True)
# #     mother=fields.Char(string='Mother', reqired=True)
# #     father=fields.Char(string='Father Name', reqired=True)
# #     image=fields.Image(string='Image' )
# #     status = fields.Selection([('Created', 'Created'),
# #                                ('Alive', 'Alive'),
# #                                ('Dead', 'Dead')], string='Status',
# #                               default='Created')
# #
# #     student_class=fields.Selection([('1', '1st'),
# #         ('2', '2nd'),
# #         ('3', '3rd '),
# #         ('4', '4th '),
# #         ('5', '5th '),
# #         ('6', '6th '),
# #         ('7', '7th '),
# #         ('8', '8th '),
# #         ('9', '9th '),
# #         ('10', '10th '),
# #         ('11', '11th '),
# #         ('+2', '+2 intermediate'),
# #         ('Graduate','Graduate'),
# #     ], string="Class Level", required=True)
# #
# #     @api.depends('DOB')
# #     def _compute_age(self):
# #         for rec in self:
# #             if rec.DOB:
# #                 today = date.today()
# #                 dob = rec.DOB
# #                 # Calculate the difference in years
# #                 age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
# #                 rec.age = age
# #             else:
# #                 rec.age = 0
# # #
# # #     @api.model
# # #     def create(self, vals):
# # #         if 'student_code' not in vals or not vals['student_code']:
# # #             vals['student_code'] = self.env['ir.sequence'].next_by_code('student.master') or '/'
# # #         return super(StudentMaster, self).create(vals)
# #
# # #
# # class SubjectMaster(models.Model):
# #     _name = 'subject.master'
# #     _description = 'Subject Master'
# #
# #     name = fields.Char(string='Subject Name', required=True)
# #     subject_code = fields.Char(string='Subject Code', required=True, unique=True)
# #     class_level = fields.Selection([
# #         ('1', '1st'),
# #         ('2', '2nd'),
# #         ('3', '3rd '),
# #         ('4', '4th '),
# #         ('5', '5th '),
# #         ('6', '6th '),
# #         ('7', '7th '),
# #         ('8', '8th '),
# #         ('9', '9th '),
# #         ('10', '10th '),
# #         ('11', '11th '),
# #         ('+2', '+2 intermediate'),
# #         ('Graduate','Graduate'),
# #     ], string="Class Level", required=True)
# #
# #
# #     # exam_marks_line_ids = fields.One2many('exam.marks.line', 'subject_id')
# #     marks = fields.Integer(string='Total Marks', required=True)
# #
# #
from odoo import models, fields, api
from datetime import date
from odoo.exceptions import UserError

class StudentMaster(models.Model):
    _name = 'student.master'
    _description = 'Student Master'

    name = fields.Char(string='Name', required=True)
    student_code = fields.Char(string='Student Code', required=True, copy=False, readonly=True, default=lambda self: self.env['ir.sequence'].next_by_code('student.master.code'))
    date_of_birth = fields.Date(string='Date of Birth', required=True)
    age = fields.Integer(string='Age', compute='_compute_age', store=True)
    mother_name = fields.Char(string="Mother's Name")
    father_name = fields.Char(string="Father's Name")
    address = fields.Text(string='Address')
    # school=fields.Many2one('student.school.history', string='School Details')
    status = fields.Selection([('active', 'Active'), ('inactive', 'Inactive')], default='active', string='Status')
    image = fields.Image(string='Student Image')
    previous_school_ids = fields.One2many('student.school.history', 'student_id', string='Previous School History')
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
        ('GRADUATE', 'B.TECH'),
    ], string="Class Level", required=True)
    @api.depends('date_of_birth')
    def _compute_age(self):
        for record in self:
            if record.date_of_birth:
                record.age = date.today().year - record.date_of_birth.year
            else:
                record.age = 0

    @api.model
    def create(self, values):
        # Get the company of the current user
        current_company = self.env.company
        restroct=[1]

        # Ensure the company matches the current user's company
        if current_company.id not in restroct :
            raise UserError("You cannot create a student record for a different company. You need to change the company")

        # Proceed with record creation
        return super(StudentMaster, self).create(values)


class StudentSchoolHistory(models.Model):
    _name = 'student.school.history'
    _description = 'Student Previous School History'
    _rec_name = "student_id"
    #
    student_id = fields.Many2one('student.master', string='Student', ondelete='cascade')
    school_name = fields.Char(string='School Name', required=True)
    syllabus_type = fields.Char(string='Syllabus Type')
    from_year = fields.Char(string='From year')
    to_year = fields.Char(string='To Year')
    marks = fields.Char(string='Mark')
    # total_marks = fields.Float(string='Total Marks Got', compute='_compute_student_marks', store=True)

    # @api.depends('student_id')
    # def _compute_student_marks(self):
    #     for record in self:
    #         # Get all the marks lines associated with the student
    #         exam_marks_lines = self.env['exam.marks.line'].search([('exam_id.student_id', '=', record.student_id.id)])
    #
    #         # Calculate total marks (you can modify this logic as per your needs)
    #         total_scored = sum(line.scored_marks for line in exam_marks_lines)
    #
    #         # Assign the total marks to the computed field
    #         record.total_marks = total_scored
    #
    # @api.model
    # def write(self, vals):
    #     if 'school_name' in vals:
    #         # Logic to handle changes in school_name
    #         # Here we could, for instance, reset the marks or perform any specific action
    #         vals['marks'] = ''  # Reset marks whenever the school name is changed (optional)
    #
    #     # Call the original write method to apply the changes
    #     return super(StudentSchoolHistory, self).write(vals)




# class SubjectMaster(models.Model):
#     _name = 'subject.master'
#     _description = 'Subject Master'
#
#     name = fields.Char(string='Subject Name', required=True)
#     subject_code = fields.Char(string='Subject Code', required=True, unique=True)
#     class_level = fields.Selection([
#         ('1', '1st'),
#         ('2', '2nd'),
#         ('3', '3rd'),
#         ('4', '4th'),
#         ('5', '5th'),
#         ('6', '6th'),
#         ('7', '7th'),
#         ('8', '8th'),
#         ('9', '9th'),
#         ('10', '10th'),
#     ], string="Class Level", required=True)
#
#     # One2many field linking to exam_marks_line
#     exam_marks_line_ids = fields.One2many('exam.marks.line', 'subject_id')
#     marks = fields.Integer(string='Total Marks', required=True)