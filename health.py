from trytond.model import fields
from trytond.pool import PoolMeta


class HealthProfessional(metaclass=PoolMeta):
    __name__ = 'gnuhealth.healthprofessional'

    es_medico = fields.Function(
        fields.Boolean('Es medico'),
        'get_es_medico'
    )

    def get_es_medico(self, name):
        if self.name:
            return bool(self.name.is_healthprof)
        return False
