'''

1) Problem Statement
--------------------------

Create a simulation to track the orbit of the Earth around the Sun for a period of 1 year.

Use Euler and Runge - Kutta method of 4th order (RK4) for this task.

Find the distance from Earth to Sun at Apogee using Euler and RK4 method and compare it with the original.

1.1) Given Equations
---------------------------


Accn of Earth due to Gravity of the Sun



ODE for Position


ODE for Velocity


1.2) Initial Condition
--------------------------


Earth is at its Perihelion (closest to Sun)


'''

# Imports
import matplotlib.pyplot as plt
import numpy as np


# Constants

G = 6.6743e-11
M_sun = 1.989e30  # kg

# Initial Position and Velocity

r_0 =  np.array([147.1e9, 0]) # m
v_0 =  np.array([0, -30.29e3]) # m/s


# Time steps and total time for simulation

dt = 3600 # s
t_max = 3.154e7 # secs


# Time array to be used in numerical solution

t = np.arange(0, t_max, dt)
# print(t.astype('int32'))     # uncomment this line to test


# Initialize arrays to store positions and velocities at all the time steps
r = np.empty(shape=(len(t), 2))
v = np.empty(shape=(len(t), 2))


# Set the Initial conditions for position and velocity

r[0], v[0] = r_0, v_0

# Drine the function that gets us the  acceleration (accn) vector when passed in the
# position vector

def accn(r):
    return(-G*M_sun / np.linalg.norm(r)**3) * r

# print(accn(r_0))    # uncomment this line to test

# Euler Integration
def euler_method(r, v, accn, dt):

 '''
    Equations for euler method
    ------------------------------
    ODE for Position
    --> dr/dt = v
    --> r_new = r_old + v_old*dt

    ODE for Velocity
    --> dv/dt = a
    --> v_new = v_old + a(r_old)*dt

    Parameters
    --------------
    r: empty array for position of size t
    v: empty array for velocity of size t
    a: func to calculate the accn at given position
    dt: time step for the simulation

    This function will update the empty arrays for r and v with the simulated data

    '''   
 

for i in range(1, len(t)):
    r[i] = r[i-1] + v[i-1] * dt
    v[i] = v[i-1] + accn(r[i-1]) * dt
    
    
    
# euler_method(r, v, accn, dt)  # uncomment these 2 lines to test
# print(r)                      # uncomment these 2 lines to test



# Apply the Euler Integration on the given conditions

euler_method(r, v, accn, dt)

# Find the point at which Earth is at its Aphelion

sizes = np.array([np.linalg.norm(position) for position in r])
pos_aphelion = np.max(sizes)
arg_aphelion = np.argmax(sizes)
vel_aphelion = np.linalg.norm(v[arg_aphelion])

print(pos_aphelion/1e9, vel_aphelion/1e3)   # uncomment this line to test
