import matplotlib.pyplot as plt
import matplotlib.animation as animation
from dataclasses import dataclass
import numpy as np

@dataclass
class State:
    net_acceleration: float
    drag: float
    time: float
    velocity: float = 0.0


time_step = 0.01


def step (state:State) -> State:
    mass = 300
    cross_sectional_area = 1.2
    drag_coefficient = 0.7
    air_density = 1.2
    acceleration = 0.0

    if state.time <= 10.0:
        acceleration = 5.0
    else:
        acceleration = 0.0


    new_drag = 0.5 * cross_sectional_area * drag_coefficient * air_density * state.velocity**2

    new_net_acceleration = acceleration - new_drag/mass

    new_velocity = state.velocity + new_net_acceleration * time_step



    return State(
        net_acceleration = new_net_acceleration,
        time = state.time + time_step,
        velocity = new_velocity,
        drag = new_drag,
    )


#if state.time > 10.0:
#    acceleration = 0.0
#    velocity = new_velocity
#    if velocity <= 0.1:
#        acceleration = 0.0
#        velocity = new_velocity
