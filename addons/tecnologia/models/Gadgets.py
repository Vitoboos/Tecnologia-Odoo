from odoo import models, fields

class Gadgets(models.Model):
    _name =   "tecnologia.gadgets"
    _description = "Accesorios"

    # Especificaciones
    type = fields.Selection([('audifonos', 'Audifonos'), ('deskphone', 'Telefono de Escritorio')], string='Tipo')
    manufacturer = fields.Char(string="Fabricante")
    model = fields.Char(string="Modelo")
    serial = fields.Char(string="Número de Serie")
    # Direccion de Red
    mac_address = fields.Char(string="Dirección MAC")
    ip_address = fields.Char(string="Dirección IP")
    # Fechas
    antiquity = fields.Char(string="Fecha de Adquisición")
    date_assigned = fields.Date(string="Fecha de Asignación")
    date_checked = fields.Date(string="Última revisión")