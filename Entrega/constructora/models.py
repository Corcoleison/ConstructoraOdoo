# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Trabajo(models.Model):
    _name = 'constructora.trabajo'

    name = fields.Char(string="Trabajo", required=True)
    descripcion = fields.Text()
    fecha = fields.Date(default=fields.Date.today, required=True)
    activo = fields.Boolean(default=True)
    lugar = fields.Char(required=True)

    responsable_id = fields.Many2one('res.partner',
        ondelete='set null', string="Responsable",  domain=['|', ('albanil', '=', True),
                     ('category_id.name', 'ilike', "responsable")])

    albaniles_ids = fields.Many2many('res.partner', string="Albañiles", domain=[('albanil', '=', True)])

    cliente_id = fields.Many2one('res.partner',
        ondelete='set null', string="Cliente", index=True)

    servicios_ids = fields.One2many(
        'constructora.servicio', 'trabajo_id', string="Servicios")

    presupuesto= fields.Float(string="Precio Total del Trabajo", compute='_computar_precio_servicios')
    
    @api.depends('servicios_ids')
    def _computar_precio_servicios(self):
        for r in self:
	 for a in r.servicios_ids:
	  precio_servicios = r.presupuesto
	  precio_material = a.preciototal
	  r.presupuesto =  precio_servicios + precio_material

class Servicio(models.Model):
    _name = 'constructora.servicio'

    name = fields.Char(string="Nombre Servicio", required=True)
    descripcion = fields.Text()
    

    
    trabajo_id = fields.Many2one('constructora.trabajo',
        ondelete='cascade', string="Trabajo")

    materiales_ids = fields.Many2many('constructora.material', string="Materiales")

    precioservicio= fields.Float(string="Precio del Servicio")
    preciomaterial= fields.Float(string="Precio total del Material", compute='_computar_precio_material_total')
    
    @api.depends('materiales_ids')
    def _computar_precio_material_total(self):
        for r in self:
	 for a in r.materiales_ids:
	  precio_material_servicio = r.preciomaterial
	  precio_material = a.preciomaterial
	  r.preciomaterial =  precio_material_servicio + precio_material

    preciototal= fields.Float(string="Precio total", compute='_computar_precio_total')

    @api.depends('precioservicio', 'preciomaterial')
    def _computar_precio_total(self):
        for r in self:
	 r.preciototal =  r.precioservicio + r.preciomaterial

class Material(models.Model):
    _name = 'constructora.material'

    name = fields.Char(string="Nombre Material", required=True)
    cantidad = fields.Integer()
    precio = fields.Float(digits=(12, 2), help="Precio por unidad")
    preciomaterial= fields.Float(string="Precio total", compute='_computar_precio_material')
    
    @api.depends('cantidad','precio')
    def _computar_precio_material(self):
        for r in self:
	 r.preciomaterial =  r.precio * r.cantidad
    
    

