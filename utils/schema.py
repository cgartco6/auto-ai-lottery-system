from dataclasses import dataclass

@dataclass
class PredictionOutput:

    top13: list
    top6: list
    simulation_size: int
