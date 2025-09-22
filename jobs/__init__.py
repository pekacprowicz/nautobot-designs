"""The __init__.py module is required for Nautobot to load the jobs via Git."""

from .core_site import CoreSiteDesign
from .pool import PoolCreateDesign
from .racks import BuildRackSwitchDesign

__all__ = [
    "CoreSiteDesign",
    "PoolCreateDesign",
    "BuildRackSwitchDesign",
]
