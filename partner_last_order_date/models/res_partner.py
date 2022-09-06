# copyright 2022 Sodexis
# license OPL-1 (see license file for full copyright and licensing details).

from odoo import models,fields,api

class Partner(models.Model):
    _inherit = "res.partner"

    date_of_last_order = fields.Date(string="Date of Last Order",compute="_compute_last_sale_confirm_date",store = True)

    @api.depends('sale_order_ids.state')
    def _compute_last_sale_confirm_date(self):
        for rec in self:
            orders = rec.sale_order_ids.filtered(lambda x :x.state in ('sale','done')).sorted(key='date_order', reverse=True)
            if orders:
                rec.date_of_last_order = orders[0].date_order
            else:
                rec.date_of_last_order = False
