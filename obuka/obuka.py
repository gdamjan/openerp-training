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
       'active' : fields.boolean('Active')
    }



obuka_session()