# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Inventory',
    'version' : '1.2',
    'summary': 'Inventory Testing Module',
    'sequence': 10,
    'description': """
This module provides a set of tools for managing inventory in Odoo. 
    """,
    'category': 'Inventory/Inventory', 
    'depends': ["base"],
    'data': [
        "views/c_stock.xml"
    ],
    'installable': True,
    'application': True,  
    'license': 'LGPL-3',
}
