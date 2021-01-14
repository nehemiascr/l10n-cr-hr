#-*- coding:utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import logging
from odoo import api, fields, models, _
from odoo.addons.report_xlsx.report.report_xlsx import ReportXlsx

_logger = logging.getLogger(__name__)


class HrPayslipRun(models.Model):
    _inherit = 'hr.payslip.run'

    def generate_payslip_run_excel_file(self):

        data = {
            'ids': self.ids,
            'model': self._name,
            'cuac': 'hola'
        }

        _logger.info('data for report_action %s' % data)

        report = self.env['report'].get_action(docids=self.ids, report_name='l10n_cr_hr_payroll.payslip_run.xlsx')
        return report
