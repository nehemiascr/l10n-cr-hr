# -*- coding: utf-8 -*-
#     dev@fakturacion.com
from odoo import api, models, fields, _
import logging
from odoo.addons.report_xlsx.report.report_xlsx import ReportXlsx

_logger = logging.getLogger(__name__)


class ReportXslxPayrollRun(ReportXlsx):

    def generate_xlsx_report(self, workbook, data, wizard):
        _logger.info('self %s workbook %s data %s wizard %s' % (self, workbook, data, wizard))

        payslip_run = self.env['hr.payslip.run'].search([('id', '=', wizard.id)])

        report_name = 'Planilla %s' % payslip_run.name
        sheet = workbook.add_worksheet(report_name)
        bold = workbook.add_format({'bold': True})

        # Report Header
        # first row : Name     Vat     Date Range
        sheet.write(0, 0, 'Tipo cuenta destino', bold)
        sheet.write(0, 1, 'Cuenta destino', bold)
        sheet.write(0, 2, 'Monto', bold)
        sheet.write(0, 3, 'Detalle', bold)
        sheet.write(0, 4, 'Correo para notificaciones', bold)

        fila = 1
        for i, payslip in enumerate(payslip_run.slip_ids):
            sheet.write(i+fila, 0, 'Cuenta de Ahorro')
            bank_account_number = ''
            if payslip.employee_id.bank_account_id and payslip.employee_id.bank_account_id.acc_number:
                bank_account_number = payslip.employee_id.bank_account_id
            sheet.write(i+fila, 1, bank_account_number)
            monto = payslip.line_ids.filtered(lambda l: l.code == 'NETO')[0].total
            sheet.write(i+fila, 2, monto)
            sheet.write(i+fila, 3, payslip.employee_id.name)
            sheet.write(i+fila, 4, payslip.employee_id.work_email or '')

ReportXslxPayrollRun('report.l10n_cr_hr_payroll.payslip_run.xlsx', 'hr.payslip.run')
