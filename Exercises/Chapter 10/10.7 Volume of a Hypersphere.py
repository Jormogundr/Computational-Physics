from random import choice

# Constants
n = 10 # number of dimensions
b = 1 # upper limit
a = -1 # lower limit

def f(space):
    r = 0
    for dim in space:
        r += dim**2
    if r <= 1:
        return 1
    else:
        return 0

def generateRndCoords():
    coords = []
    for i in range(0, n):
        t = choice(range(-1000,1000))/1000
        coords.append(t)
    return coords
    
def multiDimensionMonteCarlo():
    N = int(1E6)
    sum = 0
    for i in range(0, N):
        space = generateRndCoords()
        val = f(space)
        sum += val
    I = 2**n*sum/N
    return I

def main():
    I2 = multiDimensionMonteCarlo()
    print("Approximate integral using mean value method = {0}".format(I2))

if __name__ == '__main__':
    main()