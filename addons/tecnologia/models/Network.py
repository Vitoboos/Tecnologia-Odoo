from odoo import models, fields

class Network(models.Model):
    _name =   "tecnologia.network"
    _description = "Equipos para la gestión de la red"

    # Especificaciones
    type = fields.Selection([
    ('switch', 'Switchs'), ('router', 'Routers'),('accesspoint', 'Puntos de Acceso'),], string='Tipo')
    manufacturer = fields.Char(string="Fabricante")
    model = fields.Char(string="Modelo")
    serial = fields.Char(string="Número de Serie")
    ports = fields.Integer(string="Puertos")
    location = fields.Char(string="Ubicación")
    # Direccion de Red
    mac_address = fields.Char(string="Dirección MAC")
    ip_address = fields.Char(string="Dirección IP")
    # Fechas
    antiquity = fields.Date(string="Fecha de Adquisición")
    date_assigned = fields.Date(string="Fecha de Asignación")
    date_checked = fields.Date(string="Última revisión")