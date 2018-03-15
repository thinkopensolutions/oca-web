.. image:: https://img.shields.io/badge/licence-LGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/lgpl-3.0-standalone.html
   :alt: License: LGPL-3

===============================
Odoo 11.0 Domain Widget Preview
===============================

This module replaces the functionality of the domain widget to use a preview of
the brand new interface that will be found in Odoo 11.0.

Usage
=====

To use this module, you need to:

#. define model_id selection field like below
#. model_id = fields.Selection(selection='_list_all_models', string='Model', required=False)

    @api.model
    def _list_all_models(self):
        self._cr.execute("SELECT model, name FROM ir_model ORDER BY name")
        return self._cr.fetchall()

    so this field should be filled with all models

#    next create any of char field and use this widget as like widget="field-selector" with 2 more attributes attrs and data_model_field

#    for example if you want to apply this widget on fax field , set field readonoly till model is not set
#    <field name="fax" position="attributes">
                <attribute name="widget">field-selector</attribute>
                <attribute name="attrs">{'readonly': [('model_id','=', False)]}</attribute>
                <attribute name="data_model_field">model_id</attribute>
            </field>

