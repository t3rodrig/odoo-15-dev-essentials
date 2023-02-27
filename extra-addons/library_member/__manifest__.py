# -*- coding: utf-8 -*-
{
    'name': "Library Members",
    'summary': "Manage members borrowing books.",
    'author': "Tonalli R.",
    # 'category': 'Uncategorized',
    # 'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': ['library_app'],
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/book_view.xml',
        'views/templates.xml',
    ],
    'application': False,
}
