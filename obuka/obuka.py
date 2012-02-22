# -*- coding: utf-8 -*-
from osv import osv, fields

class obuka_session(osv.osv):
    _name = "obuka.session"
    _order = 'name'
    def _obuka_occupied(self, cr, uid, ids, name, arg, context=None):
        res = {}
        for obuka in self.browse(cr, uid, ids, context):
            #import pdb; pdb.set_trace()
            curr_partner_number = obuka.partner_number
            curr_attendees_number = len(obuka.attendee_ids)
            if curr_partner_number == 0:
                res[obuka.id] = 0
            else:
                res[obuka.id] = float(curr_attendees_number) / curr_partner_number * 100
        return res

    _columns = {
        'name': fields.char('Name', size=32, required=True,readonly=True,
            states={'draft': [('readonly', False)]}
            ),
        'description': fields.text('Description'),
        'state': fields.selection([
              ('draft', 'Draft'),
              ('done', 'Done'),
              ('cancel', 'Cancel'),
            ],'State',
            required=True,
            readonly=True),
        'responsible_id': fields.many2one('res.users', 'Responsible user'),
        'course_ids': fields.one2many('obuka.course', 'session_id', 'Course'),
        'attendee_ids': fields.many2many('res.partner',
                                        'session_partner_rel',
                                        'session_id',
                                        'partner_id',
                                        'Attendees'),
        'partner_number': fields.integer('Max number of attendees',
            required=True),
        'occupied': fields.function(_obuka_occupied,
            method=True,
            string='Occupied(%)',
            type='float', store=True)

    }
    _defaults = {
        'partner_number': 1
    }

    def session_done(self, cr, uid, ids, *args):
        self.write(cr, uid, ids, {'state':'done'})
        return True

    def session_draft(self, cr, uid, ids, *args):
        self.write(cr, uid, ids, {'state':'draft'})
        return True

    def session_cancel(self, cr, uid, ids, *args):
        self.write(cr, uid, ids, {'state':'cancel'})
        return True

    def onchange_partner_number(self, cr, uid, ids, partner_number):
        val = {}
        warn = {}
        if ids:
            len_attendees = len(self.browse(cr, uid, ids[0]).attendee_ids)
            curr_partner_number = self.browse(cr, uid, ids[0]).partner_number
            if len_attendees > partner_number:
                val['partner_number'] = curr_partner_number
                warn['title'] = 'Warning'
                warn['message'] = 'Max number of partners is too low! Returning to orginal value'
        return {'value': val, 'warning' : warn}

    def copy(self, cr, uid, id, default, context=None):
        default.update({
            'name': self.browse(cr, uid, id).name + ' (copy)'
        })
        return super(obuka_session, self).copy(cr, uid, id, default, context=context)



obuka_session()


class obuka_course(osv.osv):
    _name = 'obuka.course'

    _columns = {
       'name': fields.char('Name', size=32),
       'date': fields.date('Date'),
       'description': fields.text('Description'),
       'instructor_id': fields.many2one('res.partner', 'Instructor',
            help='Instructor that is in charge'),
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
