{
    'name': 'Hospital Management',
    'version': '0.1.0',
    'summary': 'Manage hospital patients and appointments',
    'sequence': -100,
    'category': 'Healthcare',
    'description': """
        Manage patient information such as name, contact, medical history, appointments, etc.
    """,
    'author': 'Your Name',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'views/patient_views.xml',
        'views/appointment_views.xml',
        'views/doctor_views.xml',
        'views/menus.xml',
    ],
    'demo': [],
    'images': [],
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
}
