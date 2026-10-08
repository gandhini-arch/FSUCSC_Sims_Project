import matplotlib.pyplot as plt
import matplotlib.animation as animation
from dataclasses import dataclass
import numpy as np

@dataclass
class State:
    time: float
    slip_angle: float
    lateral_velocity: float = 0.0
    

time_step = 0.01

def step (state:State) -> State:
    forward_speed = 15
    cornering_stiffness = 36000
    mass = 300

    if state.time <= 3:
        steer_angle = state.time * 5/3
    elif state.time <= 10:
        steer_angle = 5.0
    else:
        steer_angle = 5.0

    steer_radians = steer_angle * np.pi / 180

    new_slip_angle = steer_radians - state.lateral_velocity/forward_speed

    new_lateral_force = cornering_stiffness * slip_angle
    
    new_lateral_acceleration = new_lateral_force/mass
    
    new_lateral_velocity = state.lateral_velocity + new_lateral_acceleration * time_step

    new_time = state.time + time_step

    return State(
        lateral_velocity = new_lateral_velocity,
        slip_angle = new_slip_angle,
        time = new_time,
    )

