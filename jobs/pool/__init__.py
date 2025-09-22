
from nautobot.apps.jobs import register_jobs, StringVar, IPNetworkVar
from nautobot_design_builder.design_job import DesignJob

class PoolCreateDesign(DesignJob):
    class Meta:
        name = "Create IP Pool"
        description = "Design Job to create an IP prefix pool in IPAM."

    # Variables exposed to the Jinja template
    pool_cidr = IPNetworkVar(
        description="CIDR prefix for the pool (e.g. 10.0.0.0/8)",
        default="10.0.0.0/8"
    )
    status = StringVar(
        description="Prefix status (e.g. active, reserved, deprecated)",
        default="active"
    )
    p_description = StringVar(
        description="Description for the pool",
        default="IP Pool created via Design Job"
    )


register_jobs(PoolCreateDesign)
