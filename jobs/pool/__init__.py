from nautobot.apps.jobs import register_jobs
from nautobot.apps.jobs.design import DesignJob
from nautobot.apps.jobs import StringVar


class PoolCreateDesign(DesignJob):
    class Meta:
        name = "Create IP Pool"
        description = "Design Job to create an IP prefix pool in IPAM."

    # Variables exposed to the Jinja template
    pool_cidr = StringVar(
        description="CIDR prefix for the pool (e.g. 10.0.0.0/8)",
        default="10.0.0.0/8"
    )
    status = StringVar(
        description="Prefix status (e.g. active, reserved, deprecated)",
        default="active"
    )
    description = StringVar(
        description="Description for the pool",
        default="IP Pool created via Design Job"
    )

register_jobs(PoolCreateDesign)
