from numpy import array, arange
from matplotlib import pyplot as plt

# Constants
omega = 1

def harmonic(r,t):
    x = r[0]
    y = r[1] # y = dx/dt
    dxdt = y
    dydt = -omega**2*x
    return array([dxdt, dydt], float)

def anharmonic(r,t):
    x = r[0]
    y = r[1]
    dxdt = y
    dydt = -omega**2*x**3
    return array([dxdt, dydt], float)

def plot(x,y):
    plt.figure(figsize=(8, 5))
    plt.plot(x,y, label = 'theta') 
    plt.xlabel("Time, t")
    plt.ylabel("dy/dt")
    plt.title("Anharmonic Oscillator", wrap=True)
    plt.savefig("Exercises/Chapter 8/Anharmonic Oscillator.jpg", format='jpg')
    plt.show()
    return

def pltPhaseSpace(x, dxdt):
    plt.figure(figsize=(8, 5))
    plt.plot(x,dxdt, label = 'theta') 
    plt.xlabel("x")
    plt.ylabel("dx/dt")
    plt.title("Anharmonic Oscillator - Phase Space", wrap=True)
    plt.savefig("Exercises/Chapter 8/Anharmonic Oscillator - Phase Space.jpg", format='jpg')
    plt.show()
    return

if __name__ == '__main__':
    a = 0
    b = 50
    N = 1000
    h = (b-a)/N

    tpoints = arange(a,b,h)
    xpoints = [] 
    ypoints = [] # y = dx/dt

    r = array([2,0],float) # r is a vector - in this case <theta,omega>
    for t in tpoints:
        xpoints.append(r[0])
        ypoints.append(r[1])
        k1 = h*anharmonic(r,t)
        k2 = h*anharmonic(r+0.5*k1,t+0.5*h)
        k3 = h*anharmonic(r+0.5*k2,t+0.5*h)
        k4 = h*anharmonic(r+k3,t+h)
        r += (k1+2*k2+2*k3+k4)/6

    #plot(tpoints, xpoints)
    pltPhaseSpace(xpoints, ypoints)