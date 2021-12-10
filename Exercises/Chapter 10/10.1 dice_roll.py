import random

def diceRoll():
    n = random.randrange(1,7)
    m = random.randrange(1,7)
    return [n, m]


if __name__ == '__main__':
    rolls = int(1E6)
    count = 0

    for i in range(0,rolls):
        roll = diceRoll()
        if roll == [6,6]:
            count +=1

    print("Number of 6's rolled: ", count/rolls, " 1/30 is ", 1/30)
        