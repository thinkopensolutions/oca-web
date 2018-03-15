# -*- coding: utf-8 -*-
# Copyright 2017 Jairo Llopis <jairo.llopis@tecnativa.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
{
    "name": "Field Selector Widget",
    "summary": "Select fields",
    "description": """
    how to use this module
    create one selection field like
    
    model_id = fields.Selection(selection='_list_all_models', string='Model', required=False)

    @api.model
    def _list_all_models(self):
        self._cr.execute("SELECT model, name FROM ir_model ORDER BY name")
        return self._cr.fetchall()

    so this field should be filled with all models

    next create any of char field and use this widget as like widget="field-selector" with 2 more attributes attrs and data_model_field

    for example if you want to apply this widget on fax field 
    <field name="fax" widget="field-selector" data_model_field="model_id" attrs="{'invisible': [('model_id','=', False)]}">


    """,
    "version": "10.0.1.0.1",
    "category": "Extra Tools",
    "website": "https://www.tko-br.com/",
    "author": "TKO, Odoo S.A., Odoo Community Association (OCA)",
    "license": "LGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "web",
    ],
    "data": [
        "templates/assets.xml",
    ],
    "qweb": [
        "static/src/xml/templates.xml",
    ],
}
