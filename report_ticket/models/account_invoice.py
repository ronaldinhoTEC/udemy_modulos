# -*- encoding: utf-8 -*-
from odoo import models, fields, api, _


class account_invoice(models.Model):
    _inherit = 'account.move'
    

    @api.model
    def invoice_print(self):
        """ Print the invoice and mark it as sent, so that we can see more
            easily the next step of the workflow
        """
        self.ensure_one()
        self.sent = True
        return self.env.ref(
            'report_ticket.report_ticket_id').report_action(
            self)
