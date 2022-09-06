# Copyright 2022 Sodexis
# License OPL-1 (See LICENSE file for full copyright and licensing details).

{
    "name": "Partner Last Order Date",
    "summary": """This module is used to find the last confirmed sale order date.""",
    "version": "15.0.1.0.0",
    "category": "Uncategorized",
    "website": "http://sodexis.com/",
    "author": "Sodexis",
    "license": "OPL-1",
    "installable": True,
    "application": False,
    "depends": [
        'base',
        'contacts',
        'sale'
    ],
    "data": [
        "views/res_partner_view.xml",
    ],
}
