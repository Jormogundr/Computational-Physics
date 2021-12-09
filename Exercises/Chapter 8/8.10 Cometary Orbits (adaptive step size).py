import numpy as np
from matplotlib import pyplot as plt

# Constants
G = 6.67408E-11
M = 1.989E30

def f(r,t):
    x,vx,y,vy = r
    R = np.sqrt(x**2 + y**2)
    d2xd2t = -(G*M*x)/R**3
    d2yd2t = -(G*M*y)/R**3
    return np.array([d2xd2t,vx, d2yd2t, vy], float) 

def plot(x,y):
    plt.figure(figsize=(8, 5))
    plt.plot(x,y, label = 'theta') 
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Comet Position", wrap=True)
    plt.savefig("Exercises/Chapter 8/Comet Position.jpg", format='jpg')
    plt.show()
    return

if __name__ == '__main__':
    a = 0
    b = 3.156e7*50
    N = 10000
    h = (b-a)/N
    
    tpoints = np.arange(a,b,h)
    xpoints = [] 
    ypoints = [] 

    r = np.array([4E12,0,0,500],float) # r is a vector - in this case <x, vx, y, vy> in <m, m/s, m, m/s>
    for t in tpoints:
        xpoints.append(r[0])
        ypoints.append(r[2])
        k1 = h*f(r,t)
        k2 = h*f(r+0.5*k1,t+0.5*h)
        k3 = h*f(r+0.5*k2,t+0.5*h)
        k4 = h*f(r+k3,t+h)
        r += (k1+2*k2+2*k3+k4)/6

    plot(xpoints, ypoints)
    #pltPhaseSpace(xpoints, ypoints)