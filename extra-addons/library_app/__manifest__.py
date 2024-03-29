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
        "security/ir.model.access.csv",
        "views/book_view.xml",
        "views/libray_menu.xml",
        "views/book_list_template.xml",
    ],
    'application': True,
}
