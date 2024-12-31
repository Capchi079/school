# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Master',
    'version': '1.2',
    'summary': ' school & master ',
    'sequence': 10,
    'description': " ",

    'category': 'master',
    'website': '',
    'depends': ['portal'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        # 'views/menu.xml',
        'data/student_sequence.xml',
        'views/menuitem.xml',
        'views/newstudent.xml',
        'views/subjectmaster.xml',
        'views/exammark.xml',
        'views/schoolhistory.xml',
        'views/home.xml',
        'views/template1.xml',
        'views/template2.xml',

    ],

    'demo': [

    ],
    'installable': True,
    'application': True,

    'license': 'LGPL-3',
}
