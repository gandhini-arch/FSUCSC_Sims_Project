import matplotlib.pyplot as plt
import matplotlib.animation as animation
from dataclasses import dataclass
import numpy as np

@dataclass
class State:
  propulsion_force: float
  acceleration: float
  time: float
  velocity: float
  temperature: float
  heat_energy: float
     

time_step = 0.01

def step (state:State) -> State:
  max_propulsion_force = 2000
  vmax = 27
  mass = 300

  voltage = 400
  resistance = 0.5
  motor_mass = 50
  specific_heat = 385
    

  if state.time <= 3.0:
      throttle = state.time / 3.0
  elif state.time <= 23.0:
      throttle = 1.0
  else:
      throttle = 0.0


  propulsion_force = max_propulsion_force * throttle * (1 - (state.velocity/vmax))
  new_acceleration = propulsion_force / mass
  new_velocity = state.velocity + (new_acceleration * time_step)
  new_time = state.time + time_step
  
  current = voltage / resistance
  heat_power = current**2 * resistance
  heat_added = heat_power * time_step
  new_heat_energy = state.heat_energy + heat_added
  temperature_change = heat_added / (motor_mass * specific_heat)
  new_temperature = state.temperature + temperature_change

  return State(
      propulsion_force=propulsion_force,
      acceleration=new_acceleration,
      velocity=new_velocity,
      temperature=new_temperature,
      heat_energy=new_heat_energy,
      time=new_time
  )
