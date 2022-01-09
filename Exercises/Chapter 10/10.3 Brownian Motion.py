import random as rnd
import matplotlib.pyplot as plt

# Constants
L = 100 # size of the lattice
N = 1000 # number of steps 
k = 5 # number of walks to complete

# Functions
def randomStep(pos):
    i, j = pos[0], pos[1]
    rand_choice = rnd.randint(0,3)
    if rand_choice == 0:
        i -= 1 # walk left
    elif rand_choice == 1:
        j += 1 # walk up
    elif rand_choice == 2:
        i += 1 # walk right
    else: 
        j -= 1 # walk down

    # If random step puts us out of lattice, turn that random step to the opposite direction.
    if i == 0: i += 1
    if i == L: i -= 1
    if j == 0: j += 1
    if j == L: j -= 1

    return [i,j] # new position



for walk in range(0,k):
    pos = [int(L/2), int(L/2)] # initial position
    xpath, ypath = [], []
    count = 0
    while count < N:
            x, y = pos[0], pos[1]
            xpath.append(x)
            ypath.append(y)
            pos = randomStep(pos)
            count += 1
    plt.plot(xpath,ypath, label="Walk {0}".format(walk))

plt.xlim(0,L)
plt.ylim(0,L)
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("Random Walk of Particles through Lattice of Length L Starting at Center")
plt.savefig("Exercises/Chapter 10/Brownian Motion.jpg", format='jpg')
plt.show()


