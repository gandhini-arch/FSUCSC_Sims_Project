import matplotlib.pyplot as plt
import matplotlib.animation as animation
from dataclasses import dataclass
import numpy as np

@dataclass
class State:
    velocity: float
    braking_force: float
    acceleration: float = 25
    time: float

time_step = 0.01

def step (state:State) -> State:
    max_braking_capacity = 1850
    mass = 300

    if state.time <= 2.0:
        driver_input = 0.0
    else:
        driver_input = 1.0

    new_braking_force = driver_input * max_braking_capacity
    
    new_acceleration = state.acceleration - (new_braking_force/mass)
    
    new_velocity = state.velocity + (acceleration * time_step)
    
    new_time = state.time + time_step

    return State(
        velocity = new_velocity,
        braking_force = new_braking_force,
        time = new_time,
        acceleration = new_acceleration
    )
