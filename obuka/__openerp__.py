# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name" : "obuka",
    "version" : "1.0",
    "author" : "gdamjan",
    "category": 'Generic Modules',
    "description": "test test some description",
    'website': 'http://damjan.softver.org.mk',
    'init_xml': [],
    "depends" : ['base'],
    'update_xml': [
            'security/obuka_security.xml',
            'security/ir.model.access.csv',
            'obuka_view.xml',
            'partner_view.xml',
            'obuka_workflow.xml',
            'wizard/course_create_view.xml',
            ],

    'demo_xml': [],
    'test': [],
    'installable': True,
    'active': False,
}
