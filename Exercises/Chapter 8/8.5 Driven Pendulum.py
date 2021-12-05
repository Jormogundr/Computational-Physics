from math import sin, cos
from numpy import array, arange, pi
from matplotlib import pyplot as plt

# Constants
g = 9.81
l = 0.1
C = 2 # s^-1
phi = 5 # s^-1

def f(r,t):
    theta = r[0]
    omega = r[1]
    ftheta = omega
    fomega = -(g/l)*sin(theta) + (C*cos(theta)*sin(phi*t))
    return array([ftheta, fomega], float)

if __name__ == '__main__':
    a = 0.0
    b = 100
    N = 1000
    h = (b-a)/N

    tpoints = arange(a,b,h)
    theta_points = []
    omega_points = []

    r = array([0,0],float) # r is a vector - in this case <theta,omega>
    for t in tpoints:
        theta_points.append(r[0])
        omega_points.append(r[1])
        k1 = h*f(r,t)
        k2 = h*f(r+0.5*k1,t+0.5*h)
        k3 = h*f(r+0.5*k2,t+0.5*h)
        k4 = h*f(r+k3,t+h)
        r += (k1+2*k2+2*k3+k4)/6

    plt.figure(figsize=(8, 5))
    plt.plot(tpoints,omega_points, label = 'theta') 
    plt.xlabel("Time, t")
    plt.ylabel("Theta (t)")
    plt.title("Position of Nonlinear Driven Pendulum", wrap=True)
    plt.savefig("Exercises/Chapter 8/Nonlinear Pendulum - 2nd order ODE (Driven).jpg", format='jpg')
    plt.show()