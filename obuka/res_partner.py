from osv import osv, fields

class obuka_partner(osv.osv):
    #_name = 'res.partner'
    _inherit = 'res.partner'
    
    _columns = {
        'session_ids': fields.many2many('obuka.session',
                                        'session_partner_rel',
                                        'partner_id',
                                        'session_id',
                                        'Sessions attending')        
    }

obuka_partner()