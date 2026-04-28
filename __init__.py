from trytond.pool import Pool

from . import health


def register():
    Pool.register(
        health.HealthProfessional,
        module='z_health_healthprof', type_='model'
    )
