# -*- coding: utf-8 -*-
{
    'name': "Library Management",
    'summary': "Manage library catalog and book lending.",
    'author': "Tonalli R.",
    'category': "Services/Library",
    'version': '15.0.1.0.0',
    # any module necessary for this one to work correctly
    'depends': ['base'],
    'data': [
        "security/library_security.xml",
        "views/libray_menu.xml",
    ],
    'application': True,
}
