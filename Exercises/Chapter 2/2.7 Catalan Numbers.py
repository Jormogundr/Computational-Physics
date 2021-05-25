# This program prints the sequence of numbers of the Catalan sequence up to one billion
cN = 1
n = 1

while cN < 1000000000:
    cN = ((4*n+2)/(n+2))*cN
    print(cN)
    n += 1
