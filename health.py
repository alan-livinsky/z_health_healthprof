from trytond.model import fields
from trytond.pool import PoolMeta


class HealthProfessional(metaclass=PoolMeta):
    __name__ = 'gnuhealth.healthprofessional'

    party_is_healthprof = fields.Function(
        fields.Boolean('Es médico?'),
        'get_party_is_healthprof'
    )

    def get_party_is_healthprof(self, name):
        return bool(self.name and self.name.is_healthprof)
