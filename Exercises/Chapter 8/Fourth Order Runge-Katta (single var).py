"""
This program demonstrates how to use the 4th order Runge-Katta method to quickly (within low number of steps) by solving the differential equation dVout/dt = (RC)^(-1)(Vin - Vout).

In this case, the input signal is a square wave with amplitude and frequency equal to 1. The plots generated show how the choice of the resistor(R) and 
capacitor (C)  affects the attentuation of the output signal. The RC values give cutoff angular frequencies of 100, 10, and 1 respectively (RC = [0.01, 0.1, 1]). As the RC value
increases, the attenuation of these low frequency signals increases -- the amplitude of Vout decreases with increasing RC. This filter could be used to filter out bass signals. 
"""

from math import floor
from numpy import arange
from matplotlib import pyplot as plt


# The input signal to the Low pass filter is a square sin wave with amplitude and frequency equal to 1.
def Vin(t):
    if floor(2*t) % 2  == 0: 
        return 1
    else: # floor of 2t is odd
        return -1

def Vout(vout, t, RC):
    vin = Vin(t)
    return (RC)**(-1)*(vin - vout)


if __name__ == '__main__':
    a = 0.0 # initial time
    b = 10.0 # final time
    N = 1000 # number of steps
    h = (b-a)/N # length of each step over interval

    tpoints = arange(a,b,h)
    RC = [0.01, 0.1, 1]
    vout = 0.0 # initial condition
    fig, ax = plt.subplots(1, len(RC), sharex=True, sharey=False, figsize=(12,6))
    fig.suptitle('Low Pass Filter Using 4th Order Runge-Katta Method', fontsize=16)

    for i, rc in enumerate(RC):
        xpoints = []
        vout = 0.0 # initial condition
        for t in tpoints:
            xpoints.append(vout)
            k1 = h*Vout(vout,t, rc)
            k2 = h*Vout(vout+0.5*k1,t+0.5*h, rc)
            k3 = h*Vout(vout+0.5*k2,t+0.5*h, rc)
            k4 = h*Vout(vout+k3,t+h, rc)
            vout += (k1+2*k2+2*k3+k4)/6
        ax[i].plot(tpoints,xpoints)
        ax[i].set_title("RC is {0}".format(rc))
        ax[i].set_xlabel("t")
        ax[i].set_ylabel("Vout(t)")
    plt.savefig("Exercises/Chapter 8/Fourth Order Runge-Katta (single var).jpg", format='jpg')
    plt.show()
