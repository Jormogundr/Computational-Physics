h = float(input("Enter the height of the tower: "))
t = float(input("Enter the time interval, t: "))
g = 9.81
dy = g*t**2/2
if h-dy < 0:
    print ("The ball has already hit the ground. It would be", h-dy, " meters below the surface.")
else:
    print("The ball is ", h-dy, " meters above the ground")
