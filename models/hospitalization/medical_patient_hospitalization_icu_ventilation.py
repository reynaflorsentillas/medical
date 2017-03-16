from odoo import api, models, fields, _ 

class MedicalPatientHospitalizationIcuVentilation(models.Model):
    _name = 'medical.patient.hospitalization.icu.ventilation'
    _description = 'Medical Patient Hospitalization ICU Ventilation'

    icu_id = fields.Many2one(comodel_name='medical.patient.hospitalization.icu', string='Hospitalization', ondelete='cascade', required=True, select=True)
    code = fields.Char()
    type = fields.Char()
    ventilation_from = fields.Datetime()
    ventilation_to = fields.Datetime()
    duration = fields.Char()
    remarks = fields.Text()
