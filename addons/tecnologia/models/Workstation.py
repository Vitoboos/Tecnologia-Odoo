# -*- coding: utf-8 -*-
# from odoo import models, fields, api
from odoo import models, fields

class Workstation(models.Model):
    _name =   "tecnologia.workstation"
    _description = "Estaciones de Trabajo"

    # Especificaciones
    type = fields.Selection([('escritorio', 'Escritorio'), ('laptop', 'Laptop')], string='Tipo')
    manufacturer = fields.Char(string="Fabricante")
    model = fields.Char(string="Modelo")
    serial = fields.Char(string="Número de Serie")
    cpu = fields.Char(string="Procesador")
    cpu_gen = fields.Char(string="Generación")
    ram = fields.Char(string="RAM")
    ram_gen = fields.Selection([('ddr3', 'DDR3'), ('ddr4', 'DDR4'), ('ddr5', 'DDR5')], string='Generación')
    storage = fields.Char(string="Almacenamiento")
    storage_type = fields.Selection([('hdd', 'HDD'), ('ssd', 'SATA SSD'), ('nvme', 'NVME SSD')], string='Tipo de Disco')
    # Direccion de Red
    name = fields.Char(string="Nombre en Dominio")
    mac_address = fields.Char(string="Dirección MAC")
    ip_address = fields.Char(string="Dirección IP")
    # Fechas
    antiquity = fields.Date(string="Fecha de Adquisición")
    date_assigned = fields.Date(string="Fecha de Asignación")
    date_checked = fields.Date(string="Última revisión")


