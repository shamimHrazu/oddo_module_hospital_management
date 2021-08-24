from odoo import api, fields, models


class SalesOrder(models.Model):
    _inherit = "sale.order"
    sales_description= fields.Text(string="Sales description")


