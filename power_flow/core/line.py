from dataclasses import dataclass
from power_flow.core.bus import Bus

@dataclass
class Line:
    name: str
    bus_from: Bus
    bus_to: Bus
    x: float           # reactance in per unit
    rating_mw: float   # thermal rating in MW