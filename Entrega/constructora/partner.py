# -*- coding: utf-8 -*-
from openerp import fields, models

class Partner(models.Model):
    _inherit = 'res.partner'

    # Add a new column to the res.partner model, by default partners are not
    # instructors
    albanil = fields.Boolean("Albañil", default=False)

    trabajos_ids = fields.Many2many('constructora.trabajo',
        string="Trabajos", readonly=True)

    
    

