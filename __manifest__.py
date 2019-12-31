# -*- coding: utf-8 -*-
# (C) 2019 Smile (<http://www.smile.fr>)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

{
    'name': "Smile assignment",

    'summary': """
        this module is dedicated to assignment""",

    'description': """
        Long description of module's purpose
    """,

    'author': "SMILE",
    'website': "http://www.smile.eu",


    # for the full list
    'category': 'tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'analytic',
                'contacts',
                'mail',
                ],

    # always loaded
    'data': [
        'security/assignment_security.xml',
        'security/ir.model.access.csv',
        'security/profiles.xml',
        'data/nature_data.xml',
        'data/trade_data.xml',
        'data/assignment_mail.xml',
        'views/assignment_views.xml',
        'views/update.xml',
        'views/trade_views.xml',
        'views/nature_views.xml',
        'views/menus.xml',
        'report/report_assignment.xml',
        'report/report.xml',

    ],

}