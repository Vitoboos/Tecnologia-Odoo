from odoo import models, fields

class Printers(models.Model):
    _name =   "tecnologia.printers"
    _description = "Impresoras"
    # Especificaciones
    manufacturer = fields.Char(string="Fabricante")
    model = fields.Char(string="Modelo")
    serial = fields.Char(string="Número de Serie")
    rented = fields.Boolean(string="Alquilada")
    # Direccion de Red
    mac_address = fields.Char(string="Dirección MAC")
    ip_address = fields.Char(string="Dirección IP")
    # Fechas
    antiquity = fields.Date(string="Fecha de Adquisición")
    date_assigned = fields.Date(string="Fecha de Asignación")
    date_checked = fields.Date(string="Última revisión")
    # Ubicacion
    location = fields.Char("Ubicación")