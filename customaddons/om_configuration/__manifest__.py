
{
    'name': 'Configuration',
    'version': '1.0.0',
    'category': 'Configuration',
    'summary': 'Configuration module for Odoo 16',
    'description': """Configuration module for Odoo 16""",
    'author': 'Ali dong',
    'company': 'dong li',
    'maintainer': 'lidong',
    'website': 'https://www.odoomates.tech',
    'depends': ['contact'],
    'data': [
        'security/ir.model.access.csv',
        'views/city_views.xml',
        'views/menus.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
