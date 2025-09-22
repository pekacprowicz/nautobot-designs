
from nautobot.apps.jobs import register_jobs, StringVar, JSONVar
from nautobot_design_builder.design_job import DesignJob

from .context import RacksCreationContext

class BuildRackSwitchDesign(DesignJob):
    class Meta:
        name = "Build Rack + Switch"
        description = "Design Job to create a rack, switch, interfaces, and assign IPs."
        design_file = "designs/0001_design.yaml.j2"
        context_class = RacksCreationContext
        nautobot_version = ">=2"

    # Location
    site_name = StringVar(
        label="Site name",
        default="LAB-WAW1"
    )
    rack_name = StringVar(
        label="Rack name",
        default="RACK-01"
    )

    # Device
    device_name = StringVar(
        label="Device name",
        default="sw01"
    )
    manufacturer_name = StringVar(
        label="Manufacturer",
        default="Generic"
    )
    devicetype_model = StringVar(
        label="DeviceType model",
        default="Generic Switch 48p"
    )
    devicerole_name = StringVar(
        label="Device role",
        default="switch"
    )

    # Interfaces list (JSON for structured data)
    interfaces = JSONVar(
        label="Interfaces",
        description="List of interfaces (JSON array of objects, e.g. [{'name': 'eth1'}, {'name': 'eth2'}])",
        default=[{"name": "eth1"}, {"name": "eth2"}]
    )

    # IP bindings (interface → address)
    ip_bindings = JSONVar(
        label="IP bindings",
        description="List of IP bindings (e.g. [{'if_name': 'eth1', 'address': '10.0.0.1/8'}])",
        default=[{"if_name": "eth1", "address": "10.0.0.1/8"}]
    )


register_jobs(BuildRackSwitchDesign)
