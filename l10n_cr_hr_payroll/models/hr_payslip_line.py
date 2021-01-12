#-*- coding:utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models, _


class HrPayslipLine(models.Model):
    _inherit = 'hr.payslip.line'

    move_id = fields.Many2one(comodel_name='account.move', related='slip_id.move_id',  store=False, copy=False)
    state = fields.Selection(related="slip_id.state", store=False, copy=False)