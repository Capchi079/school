from odoo import models, fields, api
import base64


# #
# from odoo.addons.test_base_import.models.test_base_import import model
# from odoo import api,fields,models
# import base64
# class ExamMarks(models.Model):
#     _name = 'exam.marks'
#     _description = 'Exam Marks'
#
#     student_id = fields.Many2one('student.master', string="Student", required=True)
#     exam_date = fields.Date(string="Exam Date", required=True)
#     marks_line_ids = fields.One2many('exam.marks.line', 'exam_id', string="Marks Line")
#     scored_marks = fields.Float(string="Scored Marks", store=True)
#     student_code = fields.Char(string='Student Code', compute='_compute_student_details', store=True, readonly=True)
#     class_level = fields.Char(string='Class', compute='_compute_student_details', store=True, readonly=True)
#     image = fields.Image(string='Image', compute='_compute_student_details', store=True, readonly=True)
#     total_subject_marks = fields.Integer(string='Total Subject Marks', compute='_compute_total_marks', store=True)
#     total_scored_marks = fields.Integer(string='Result', compute='_compute_total_marks', store=True)
#     percentage = fields.Float(string='Percentage %', compute='_compute_percentage_and_grade', store=True)
#     grade = fields.Char(string='Grade', compute='_compute_percentage_and_grade', store=True)
#
#     @api.depends('total_subject_marks', 'total_scored_marks')
#     def _compute_percentage_and_grade(self):
#         for record in self:
#             if record.total_subject_marks > 0:
#                 # Calculate percentage
#                 record.percentage = (record.total_scored_marks / record.total_subject_marks) * 100
#
#                 # Calculate grade based on percentage
#                 if record.percentage >= 90:
#                     record.grade = 'exlent '
#                 elif record.percentage >= 75:
#                     record.grade = 'good'
#                 elif record.percentage >= 60:
#                     record.grade = 'avarage'
#                 elif record.percentage >= 40:
#                     record.grade = 'need to improve'
#                 elif record.percentage >= 1:
#                     record.grade = 'Fail'
#                 else:
#                     record.grade = '0'
#             else:
#                 record.percentage = 0.0
#                 record.grade = 'N/A'
#
#
#     @api.depends('marks_line_ids.subject_marks', 'marks_line_ids.scored_marks')
#     def _compute_total_marks(self):
#         for record in self:
#             total_subject = sum(line.subject_marks for line in record.marks_line_ids)
#             total_scored = sum(line.scored_marks for line in record.marks_line_ids)
#             record.total_subject_marks = total_subject
#             record.total_scored_marks = total_scored
#
#     @api.depends('student_id')
#     def _compute_student_details(self):
#         for rec in self:
#             if rec.student_id:
#                 rec.student_code = rec.student_id.student_code
#                 rec.class_level = rec.student_id.class_level
#                 rec.image = self._validate_image(rec.student_id.image)
#             else:
#                 rec.student_code = ''
#                 rec.class_level = ''
#                 rec.image = False  # Use False for images
#
#     @staticmethod
#     def _validate_image(image_data):
#         """Check if image data is valid base64."""
#         if image_data and isinstance(image_data, str):
#             try:
#                 base64.b64decode(image_data, validate=True)
#                 return image_data  # Return original if valid
#             except Exception:
#                 return False  # Return False if invalid
#         return False  # Return False if no data
#
#
# class ExamMarksLine(models.Model):
#     _name = 'exam.marks.line'
#     _description = 'Exam Marks Line'
#
#     exam_id = fields.Many2one('exam.marks', string="Exam", required=True)
#     subject_id = fields.Many2one('subject.master', string='Subject', required=True)
#     scored_marks = fields.Float(string="Scored Marks", required=True)
#     subject_marks = fields.Integer(string='Total Marks', compute='_compute_subject_details', store=True, readonly=True)
#     percentage = fields.Float(string='Percentage %', compute='_compute_percentage_and_grade', store=True)
#     grade = fields.Char(string='Grade', compute='_compute_percentage_and_grade', store=True)
#
#     @api.depends('subject_marks', 'scored_marks')
#     def _compute_percentage_and_grade(self):
#         for record in self:
#             if record.subject_marks > 0:
#                 # Calculate percentage
#                 record.percentage = (record.scored_marks / record.subject_marks) * 100
#
#                 # Calculate grade based on percentage
#                 if record.percentage >= 90:
#                     record.grade = 'Grade A'
#                 elif record.percentage >= 75:
#                     record.grade = 'Grade B'
#                 elif record.percentage >= 60:
#                     record.grade = 'Grade C'
#                 elif record.percentage >= 40:
#                     record.grade = 'Grade D'
#                 elif record.percentage >= 1:
#                     record.grade = 'Fail'
#                 elif record.percentage <= 0:
#                     record.grade = '0'
#                 else:
#                     record.grade = '0'
#             else:
#                 record.percentage = 0.0
#                 record.grade = 'N/A'
#
#     @api.depends('subject_id')
#     def _compute_subject_details(self):
#         for rec in self:
#             if rec.subject_id:
#                 rec.subject_marks = rec.subject_id.marks  # Assuming 'class_level' is a field in the student model
#             else:
#                 rec.subject_marks = ''
# #

class ExamMarks(models.Model):
    _name = 'exam.marks'
    _description = 'Exam Marks Calculation'
    _rec_name = 'student_id'

    student_id = fields.Many2one('student.master', string="Student", required=True)
    exam_date = fields.Date(string="Exam Date", required=True)
    marks_line_ids = fields.One2many('exam.marks.line', 'exam_id', string="Marks Line")
    scored_marks = fields.Float(string="Scored Marks", store=True)
    student_code = fields.Char(string='Student Code', compute='_compute_student_details', store=True, readonly=True)
    class_level = fields.Char(string='Class', compute='_compute_student_details', store=True, readonly=True)
    image = fields.Image(string='Image', compute='_compute_student_details', store=True, readonly=True)
    total_subject_marks = fields.Integer(string='Total Subject Marks', compute='_compute_total_marks', store=True)
    total_scored_marks = fields.Integer(string='Result', compute='_compute_total_marks', store=True)
    percentage = fields.Float(string='Percentage %', compute='_compute_percentage_and_grade', store=True)
    grade = fields.Char(string='Grade', compute='_compute_percentage_and_grade', store=True)

    @api.depends('total_subject_marks', 'total_scored_marks')
    def _compute_percentage_and_grade(self):
        for record in self:
            if record.total_subject_marks > 0:
                # Calculate percentage
                record.percentage = (record.total_scored_marks / record.total_subject_marks) * 100

                # Calculate grade based on percentage
                if record.percentage >= 90:
                    record.grade = 'Grade A'
                elif record.percentage >= 75:
                    record.grade = 'Grade B'
                elif record.percentage >= 60:
                    record.grade = 'Grade C'
                elif record.percentage >= 40:
                    record.grade = 'Grade D'
                elif record.percentage >= 1:
                    record.grade = 'Fail'
                else:
                    record.grade = '0'
            else:
                record.percentage = 0.0
                record.grade = 'N/A'


    @api.depends('marks_line_ids.subject_marks', 'marks_line_ids.scored_marks')
    def _compute_total_marks(self):
        for record in self:
            total_subject = sum(line.subject_marks for line in record.marks_line_ids)
            total_scored = sum(line.scored_marks for line in record.marks_line_ids)
            record.total_subject_marks = total_subject
            record.total_scored_marks = total_scored


    @api.depends('student_id')
    def _compute_student_details(self):
        for rec in self:
            if rec.student_id:
                rec.student_code = rec.student_id.student_code
                rec.class_level = rec.student_id.class_level
                # rec.image = self._validate_image(rec.student_id.image)
            else:
                rec.student_code = ''
                rec.class_level = ''
                rec.image = False  # Use False for images


    # def _validate_image(self, image_data):
    #     """Check if image data is valid base64."""
    #     if image_data and isinstance(image_data, str):
    #         try:
    #             base64.b64decode(image_data, validate=True)
    #             return image_data  # Return original if valid
    #         except Exception:
    #             return False  # Return False if invalid
    #     return False  # Return False if no data
    #

class ExamMarksLine(models.Model):
    _name = 'exam.marks.line'
    _description = 'Exam Marks Details'

    exam_id = fields.Many2one('exam.marks', string="Exam", required=True)
    subject_id = fields.Many2one('subject.master', string='Subject', required=True)
    scored_marks = fields.Float(string="Scored Marks", required=True)
    subject_marks = fields.Integer(string='Total Marks', compute='_compute_subject_details', store=True, readonly=True)
    percentage = fields.Float(string='Percentage %', compute='_compute_percentage_and_grade', store=True)
    grade = fields.Char(string='Grade', compute='_compute_percentage_and_grade', store=True)

    @api.depends('subject_marks', 'scored_marks')
    def _compute_percentage_and_grade(self):
        for record in self:
            if record.subject_marks > 0:
                # Calculate percentage
                record.percentage = (record.scored_marks / record.subject_marks) * 100

                # Calculate grade based on percentage
                if record.percentage >= 90:
                    record.grade = 'Grade A'
                elif record.percentage >= 75:
                    record.grade = 'Grade B'
                elif record.percentage >= 60:
                    record.grade = 'Grade C'
                elif record.percentage >= 40:
                    record.grade = 'Grade D'
                elif record.percentage >= 1:
                    record.grade = 'Fail'
                elif record.percentage <= 0:
                    record.grade = '0'
                else:
                    record.grade = '0'
            else:
                record.percentage = 0.0
                record.grade = 'N/A'

    @api.depends('subject_id')
    def _compute_subject_details(self):
        for rec in self:
            if rec.subject_id:
                rec.subject_marks = rec.subject_id.marks  # Assuming 'class_level' is a field in the student model
            else:
                rec.subject_marks = ''