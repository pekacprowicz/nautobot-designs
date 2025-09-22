
from nautobot.apps.jobs import register_jobs, StringVar, JSONVar
from nautobot_design_builder.design_job import DesignJob

class BuildRackSwitchDesign(DesignJob):
    class Meta:
        name = "Build Rack + Switch"
        description = "Design Job to create a rack, switch, interfaces, and assign IPs."

    # Location
    site_name = StringVar(
        description="Site name (will be created if missing)",
        default="LAB-WAW1"
    )
    rack_name = StringVar(
        description="Rack name (will be created if missing)",
        default="RACK-01"
    )

    # Device
    device_name = StringVar(
        description="Device name",
        default="sw01"
    )
    manufacturer_name = StringVar(
        description="Manufacturer",
        default="Generic"
    )
    devicetype_model = StringVar(
        description="DeviceType model",
        default="Generic Switch 48p"
    )
    devicerole_name = StringVar(
        description="Device role",
        default="switch"
    )

    # Interfaces list (JSON for structured data)
    interfaces = JSONVar(
        description="List of interfaces (JSON array of objects, e.g. [{'name': 'eth1'}, {'name': 'eth2'}])",
        default=[{"name": "eth1"}, {"name": "eth2"}]
    )

    # IP bindings (interface → address)
    ip_bindings = JSONVar(
        description="List of IP bindings (e.g. [{'if_name': 'eth1', 'address': '10.0.0.1/8'}])",
        default=[{"if_name": "eth1", "address": "10.0.0.1/8"}]
    )


register_jobs(BuildRackSwitchDesign)
