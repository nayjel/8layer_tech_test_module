{
    'name'          : '8layer_tech_test_module',
    'version'       : 'v.1.0', 
    'summary'       : '8layer_tech_test_module',
    'website'       : '8layer_tech_test_module',
    'sequence'      : 1,
    'author'        : 'N. Calsa',
    'description'   : """
                      8layer_tech_test_module
                      """,
    'category'      : 'field',
    'depends'       : ['base', 'account', 'sale'],
    'data'          : [
                        'views/test_module_custom_form_view.xml',
                        'views/test_module_custom_tree_view.xml',
                      ],
    'installable'   : True,                  
    'application'   : True,
    'auto_install'  : False
}

# 'security/ir.model.access.csv'