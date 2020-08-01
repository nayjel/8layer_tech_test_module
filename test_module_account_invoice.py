from odoo import api,fields,models,_


class test_module(models.Model):
    _inherit = "account.move"

    test_field = fields.Many2one('res.partner', 'VENDOR')


                

    