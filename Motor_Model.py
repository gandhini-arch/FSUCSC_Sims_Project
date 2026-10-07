import matplotlib.pyplot as plt
import matplotlib.animation as animation
from dataclasses import dataclass
import numpy as np

@dataclass
class State:
    propulsion_force: float
    acceleration: float
    time: float
    velocity: float = 0

time_step = 0.01

def step (state:State) -> State:
    max_propulsion_force = 2000
    vmax = 27
    mass = 300


    if state.time <= 3.0:
        throttle = state.time / 3.0
    elif state.time <= 23.0:
        throttle = 1.0
    else:
        throttle = 0.0


    propulsion_force = max_propulsion_force * throttle * (1 - (state.velocity/vmax))
    new_acceleration = propulsion_force / mass
    new_velocity = state.velocity + (new_acceleration * time_step)


    return State(
        propulsion_force = propulsion_force,
        acceleration = new_acceleration,
        velocity = new_velocity,
        time = state.time + time_step,
    )

