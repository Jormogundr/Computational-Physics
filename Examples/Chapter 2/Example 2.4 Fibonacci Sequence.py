# This program generates the fibonacci sequence up to 1 billion
f1 = 1
f2 = 1
while f1 < 1000000000:
    fNext = f1 + f2
    f1 = f2
    f2 = fNext
    print(f1)
