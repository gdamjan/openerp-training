from osv import osv, fields

class course_create(osv.osv_memory):
    _name = 'obuka.course.create'
    _description = 'Create courses'

    _columns = {
        'course_number': fields.integer('Number of courses', required=True),
        'instructor_id': fields.many2one('res.partner', 'Instructor', required=True)
    }

    _defaults = {
        'course_number': 5,
    }

    def create_courses(self, cr, uid, ids, context=None):
        course_obj = self.pool.get('obuka.course')
        course_number = self.browse(cr, uid, ids[0], context).course_number
        instructor = self.browse(cr, uid, ids[0], context).instructor_id.id

        for i in range(course_number):
            num = i + 1
            new_course = {
                'name':'Course %d' % num,
                'description': 'Course created by wizard with poz %d' % num,
                'session_id': context['active_id'],
                'instructor_id': instructor
            }
            course_obj.create(cr, uid, new_course)

        return {'type':'ir.actions.act_window_close'}


course_create()
