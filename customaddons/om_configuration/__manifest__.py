
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
    'depends': ['base','contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/city_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
