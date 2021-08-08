#-*- coding:utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
# nehemias@automatuanis.com
import logging
from odoo import api, models

_logger = logging.getLogger(__name__)


class HrPayslip(models.Model):
    _inherit = 'hr.payslip'

    @api.model
    def get_worked_day_lines(self, contracts, date_from, date_to):
        """ Remove all non-alphanumeric characters from the 'code' field
            so they can be used in salary rules
        """
        res = super(HrPayslip, self).get_worked_day_lines(contracts, date_from, date_to)
        for line in res:
            line['code'] = re.sub(r'[^A-Za-z0-9]+', '_', line['code'])
        return res
