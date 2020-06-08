# -*- coding: utf-8 -*-
##############################################################################
#    License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
#    Copyright (C) 2019 Comunitea Servicios Tecnológicos S.L. All Rights Reserved
#    Vicente Ángel Gutiérrez <vicente@comunitea.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
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

from odoo import api, models, fields
import logging

_logger = logging.getLogger(__name__)

class ProductProduct(models.Model):
    _inherit = 'product.product'

    wh_code = fields.Char(string='Unique WH Code', compute="_compute_wh_code", store=True)
    code_ignored = fields.Char(string="Codes to ignore as Serial")

    @api.multi
    @api.depends('default_code', 'barcode')
    def _compute_wh_code(self):
        for product in self:
            if product.barcode:
                product.wh_code = product.barcode
            elif product.default_code:
                product.wh_code = product.default_code
            else:
                bind_id = product.prestashop_bind_ids and product.prestashop_bind_ids[0]
                if bind_id:
                    product.wh_code = '.%06d.'%bind_id.prestashop_id
                else:
                    product.wh_code = '.9%05d.' %product.id
            print ("Wh code para el producto {}: {}".format(product.default_code, product.wh_code))

    def return_fields(self, mode='tree'):
        return ['id', 'display_name', 'default_code', 'list_price', 'qty_available', 'virtual_available', 'tracking', 'wh_code']

    def m2o_dict(self, field):
        if field:
            return {'id': field.id, 'name': field.apk_name, 'default_code': field.default_code, 'barcode': field.barcode, 'wh_code': field.wh_code}
        else:
            return {'id': False}



