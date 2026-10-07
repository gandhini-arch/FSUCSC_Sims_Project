import matplotlib.pyplot as plt
import matplotlib.animation as animation
from dataclasses import dataclass
import numpy as np

@dataclass
class State:
    steer_angle: float
    time: float
    slip_angle: float
    lateral_force: float
    lateral_acceleration: float
    lateral_velocity: float = 0.0

time_step = 0.01

def step (state:State) -> State:
    forward_speed = 15
    cornering_stiffness = 36000
    mass = 300
    steer_angle = state.steer_angle

    if state.time <= 3:
        steer_angle = state.time * 5/3
    elif state.time <= 10:
        steer_angle = 5.0
    else:
        steer_angle = state.steer_angle

    steer_radians = steer_angle * np.pi / 180

    slip_angle = steer_radians - state.lateral_velocity/forward_speed

    new_lateral_force = cornering_stiffness * slip_angle
    
    new_lateral_acceleration = new_lateral_force/mass
    
    new_lateral_velocity = state.lateral_velocity + new_lateral_acceleration * time_step

    return State(
        lateral_velocity = new_lateral_velocity,
        steer_angle = steer_angle,
        time = state.time + time_step,
        slip_angle = slip_angle,
        lateral_force = new_lateral_force,
        lateral_acceleration = new_lateral_acceleration
    )

