# -*- coding: utf-8 -*-
from openerp import models, fields, api
class TodoTask(models.Model):
    _name = 'todo.task'
    name = fields.Char('Description', required=True)
    is_done = fields.Boolean('Done?')
    active = fields.Boolean('Active?', default=True)

    @api.one
    def do_toggle_done(self):
        if self.user_id != self.env.user:
            raise Exception('Only the Responsible can do this!')
        else:
            return super(TodoTask,self).do_toggle_done()

    @api.multi
    def do_clear_done(self):
        domain = [('is_done','=',True),
            '|',('user_id','=',self.env.uid),
            ('user_id','=',False)]
            done_recs = self.search(domain)
            done_recs.write({'active':False})
        return True
