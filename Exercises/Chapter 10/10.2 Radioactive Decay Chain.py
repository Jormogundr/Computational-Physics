from random import random
from numpy import arange
from pylab import plot,xlabel,ylabel,show,legend

# Constants
# Number of atoms in sample initially
NBi213, NBi209, NTl, NPb = 1000, 0, 0, 0    

# Half lives
tau_Bi213, tau_Tl, tau_Pb = 46*60, 2.2*60, 3.3*60
dt = 1.0               # Size of time-step in seconds
p_Bi213, p_Tl, p_Pb = 1 - 2**(-dt/tau_Bi213),  1 - 1 - 2**(-dt/tau_Tl), 1 - 2**(-dt/tau_Pb)  # Probability of decay in one step
tmax = 1000           # Total time

# Lists of plot points
tpoints = arange(0.0,tmax,dt)
Tlpoints = []
Pbpoints = []
NBi209points = []
NBi213points = []

# Main loop
for t in tpoints:
    Tlpoints.append(NTl)
    Pbpoints.append(NPb)
    NBi209points.append(NBi209)
    NBi213points.append(NBi213)

    # Calculate the number of atoms that decay
    decay_Bi213, decay_Tl, decay_Pb = 0, 0, 0

    for i in range(NBi213):
        # The order of these conditionals is important. The bottom-to-top approach ensures the same atom can't decay more than once at a single timestep.
        # Pb check - decay to Bi209 or not
        if random()<p_Pb and NPb > 0:
            NPb -= 1
            NBi209 += 1

        # Tl check - decay to to Pb or not
        if random()<p_Tl and NTl > 0:
            NTl -= 1
            NPb += 1

        # Bi209 check - decay to Tl or Pb or not
        if random()<p_Bi213:
            NBi213 -= 1
            if random()<0.0209: # Bi213 decays to Tl with 2.09% probability or to Pb with 97.91% probability
                NTl += 1
            else:
                NPb += 1

# Make the graph
print("NBi213 ", NBi213, " NBi209 ", NBi209, " NTl ", NTl, " NPb ", NPb, " Total = ", NBi209 + NBi213 + NTl + NPb )
plot(tpoints,NBi209points, label='Bi209')
plot(tpoints,Pbpoints, label='Pb')
plot(tpoints,Tlpoints, label='Tl')
plot(tpoints,NBi213points, label='Bi213')
xlabel("Time")
ylabel("Number of atoms")
legend()
show()
