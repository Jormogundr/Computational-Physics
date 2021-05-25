from math import sin,cos,radians,pi

## This program converts polar coordinates on a 2D plane to cartesian.

r = float(input("Enter the value for the distance, r: "))
theta = float(input("Enter the value for the angle, theta: "))
## Assume that theta is given in degrees. Two methods for converting degrees to radians is below.

thetaRad = radians(theta)
thetaRadAlt = theta*(pi/180)


x = r*cos(thetaRadAlt)
y = r*sin(thetaRadAlt)

print("The value for x is ", x, "and the value for y is ", y)
