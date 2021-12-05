"""
This program demonstrates the implementation of the Runge-Katta 4th order method by applying it to solve the Lotka-Volterra equations, which model populations of predator/prey species and how
the growth/decline of one has such an affect on the other members of the ecosystem being modelled. 

The rabbit population (x) and fox population (y) make up the vector r(x,y). The equations in this case are time independent, nonetheless we still plot their population against time.

Then, dr/dt = f(r(x,y),t) -- where f is a vector valued function f = <fx, fy>.

First we define some growth constants, then implement RK4. The plot is generated as well.
"""
from numpy import array,arange
from matplotlib import pyplot as plt

# Growth constants.
gamma, r_const, b_const = 10, 28, 8/3

# Rabbit (x) and fox (y) population growth. The rate of growth functions do not depend on t - only on the populations of their own and the other species.
def f(r,t):
    x = r[0] # extract x component from vector r
    y = r[1] # extract y component from vector r
    z = r[2] # extract z component from vector r
    fx = gamma*(y-x) # fx(x,y,z,t)
    fy = (r_const*x) - y - (x*z) # fy(x,y,z,t)
    fz = (x*y) - (b_const*z) # fz(x,y,z,t)
    return array([fx,fy, fz],float) # return a vector valued function F = <fx, fy, fz>

a = 0.0
b = 50.0
N = 1000
h = (b-a)/N

tpoints = arange(a,b,h)
xpoints = []
ypoints = []
zpoints = []

r = array([0.0,1.0,0.0],float) # r is a vector - in this case <x,y,z>. These define the initial conditions.
for t in tpoints:
    xpoints.append(r[0])
    ypoints.append(r[1])
    zpoints.append(r[2])
    k1 = h*f(r,t)
    k2 = h*f(r+0.5*k1,t+0.5*h)
    k3 = h*f(r+0.5*k2,t+0.5*h)
    k4 = h*f(r+k3,t+h)
    r += (k1+2*k2+2*k3+k4)/6
plt.figure(figsize=(8, 5))
plt.plot(xpoints,zpoints, label= 'z') 
plt.xlabel("x")
plt.ylabel("z(x)")
plt.title("Lorenz Equations - Random Behavior from Deterministic Functions (Strange Attractor)", wrap=True)
plt.savefig("Exercises/Chapter 8/Lorenz - RK4 Multivariate.jpg", format='jpg')
plt.show()
