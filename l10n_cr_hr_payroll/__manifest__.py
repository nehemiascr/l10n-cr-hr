#-*- coding:utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    'name': 'Costa Rica Payroll',
    'version': '12.0.1.0.1',
    'category': 'Human Resources',
    'author': 'Odoo CR Team, Odoo Community Association (OCA)',
    'license': 'AGPL-3',
    'installable': True,
    'application': False,
    'sumary': 'Costa Rica Payroll Rules',
    'depends': [
        'hr_payroll', 'to_hr_salary_rule_datetime_libs',
    ],
    'data': [
        'data/hr_contribution_register_data.xml',
        'data/hr_salary_rule_category_data.xml',
        'data/hr_salary_rule_data.xml',
        'data/hr_payroll_structure_data.xml',

        'views/hr_payslip_line_views.xml',
        'views/hr_payslip_run_views.xml',
        'views/hr_payslip_views.xml',
    ],
}
