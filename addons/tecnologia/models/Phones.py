from odoo import models, fields

class Phones(models.Model):
    _name =   "tecnologia.phones"
    _description = "Teléfonos"
    # Especificaciones
    manufacturer = fields.Char(string="Fabricante")
    model = fields.Char(string="Modelo")
    serial = fields.Char(string="Número de Serie")
    release = fields.Integer(string = "Año de Fabricación")
    # Identificación
    number = fields.Char(string="Número Teléfonico")
    imei1 = fields.Char(string="IMEI 1")
    imei2 = fields.Char(string="IMEI 2")
    # Direccion de Red
    mac_address = fields.Char(string="Dirección MAC")
    ip_address = fields.Char(string="Dirección IP")
    # Fechas
    antiquity = fields.Date(string="Fecha de Adquisición")
    date_assigned = fields.Date(string="Fecha de Asignación")
    date_checked = fields.Date(string="Última revisión")