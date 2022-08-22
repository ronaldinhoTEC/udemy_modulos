# -*- encoding: utf-8 -*-
from odoo import models, fields, api, _


class account_invoice(models.Model):
    _inherit = ['sale.order']
    # serie = fields.Char(string='Serie', related = 'picking_id.serie', readonly=True)

    @api.model
    def invoice_print(self):
        """ Print the invoice and mark it as sent, so that we can see more
            easily the next step of the workflow
        """
        self.ensure_one()
        self.sent = True
        return self.env.ref(
            'mi_reporte.report_ticket_id').report_action(
            self)
