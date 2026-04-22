from trytond.pool import Pool

from . import health


def register():
    Pool.register(
        health.HealthProfessional,
        module='health_view_custom', type_='model'
    )
