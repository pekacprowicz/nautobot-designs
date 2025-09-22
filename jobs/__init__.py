"""The __init__.py module is required for Nautobot to load the jobs via Git."""

from .core_site import CoreSiteDesign
from .pool import PoolDesign
from .racks import RacksDesign

__all__ = [
    "CoreSiteDesign",
    "PoolCreateDesign",
    "BuildRackSwitchDesign",
]
