# -*- coding: utf-8 -*-
{
    'name': "Library Members",
    'summary': "Manage members borrowing books.",
    'author': "Tonalli R.",
    # 'category': 'Uncategorized',
    # 'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': ['library_app', 'mail'],
    # always loaded
    'data': [
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/book_view.xml',
        'views/member_view.xml',
        'views/library_menu.xml',
        'views/book_list_template.xml',
    ],
    'application': False,
}
