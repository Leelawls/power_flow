from dataclasses import dataclass

@dataclass
class Bus:
    name: str
    x_coord: float
    y_coord: float
    p_injection: float  # MW, positive = generation, negative = load
    angle: float        # radians

    def __repr__(self) -> str:
        return f"Bus(name={self.name}, angle={self.angle:.4f} rad, P={self.p_injection} MW)"
