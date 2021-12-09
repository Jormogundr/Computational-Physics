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
alpha, beta, gamma, delta = 1, 0.5, 0.5, 2

# Rabbit (x) and fox (y) population growth. The rate of growth functions do not depend on t - only on the populations of their own and the other species.
def f(r,t):
    x = r[0]
    y = r[1] 
    fx = (alpha*x) - (beta*x*y) # fx(x,y,t)
    fy = (gamma*x*y) - (delta*y) # fy(x,y,t)
    return array([fx,fy],float) # return a vector valued function <fx(x,y,t), fy(x,y,t)>

a = 0.0
b = 30.0
N = 1000
h = (b-a)/N

tpoints = arange(a,b,h)
xpoints = []
ypoints = []

r = array([2.0,2.0],float) # r is a vector - in this case <x,y>
for t in tpoints:
    xpoints.append(r[0])
    ypoints.append(r[1])
    k1 = h*f(r,t)
    k2 = h*f(r+0.5*k1,t+0.5*h)
    k3 = h*f(r+0.5*k2,t+0.5*h)
    k4 = h*f(r+k3,t+h)
    r += (k1+2*k2+2*k3+k4)/6
plt.figure(figsize=(8, 5))
plt.plot(tpoints,xpoints, label = 'x, rabbits') # Rabbit growth curve
plt.plot(tpoints,ypoints, label= 'y, foxes') # Fox growth curve
plt.xlabel("Time, t")
plt.ylabel("Population growth")
plt.title("Lotka-Volterra Equations: Co-dependent Population Growth Between Rabbits (x) and Foxes(y)", wrap=True)
plt.legend()
plt.savefig("Exercises/Chapter 8/Lotka-Volterra - RK4 Multivariate.jpg", format='jpg')
plt.show()
