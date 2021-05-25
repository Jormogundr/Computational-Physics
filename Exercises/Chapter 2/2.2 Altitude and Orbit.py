import math

G = 6.67e-11
M = 5.97e24
R = 6.371e6
p = 3.14

while True:
    T = float(input("Enter the orbital time, T, in seconds: "))
    print(G,M,R,p,T,sep="   ")
    if(T == 0):
        break
    h = ((G*M*T**2)/(4*p**2))**(1/3)
    alt = h-R
    alt_km = alt/1000 
    print("The calculated altitude is ", alt, " meters. Or ", alt_km, " km.")

    
