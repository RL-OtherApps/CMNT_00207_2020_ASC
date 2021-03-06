# © 2020 Comunitea
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import fields, models


class AccountInvoice(models.Model):

    _inherit = 'account.invoice'

    mail_sended = fields.Boolean()
