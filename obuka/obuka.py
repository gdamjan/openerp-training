# -*- coding: utf-8 -*-
from osv import osv, fields

class obuka_session(osv.osv):
    _name = "obuka.session"
    _columns = {
       'name': fields.char('Name', size=32, required=True),
       'description': fields.text('Description'),
       'state': fields.selection([
            ('draft', 'Draft'),
            ('done', 'Done'),
            ('cancel', 'Cancel'),
        ],
        'State',
        required=True),
       'responsible_id': fields.many2one('res.users', 'Responsible user'),
       'course_ids': fields.one2many('obuka.course', 'session_id', 'Course')
    }

obuka_session()


class obuka_course(osv.osv):
    _name = 'obuka.course'

    _columns = {
       'name': fields.char('Name', size=32),
       'date': fields.date('Date'),
       'description': fields.text('Description'),
       'instructor_id': fields.many2one('res.partner', 'Instructor'),
       'max_users': fields.integer('Max users'),
       'session_id': fields.many2one('obuka.session', 'Session')
    }
    
    _defaults = {
       'max_users':10
    }
    
    _sql_constraints = [
        ('max_max_users', 'CHECK(max_users<50)', 'Max users limit exceeded'),
    ]

obuka_course()