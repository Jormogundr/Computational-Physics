## this program calculates the transmission and reflection probabilities of a quantum particle incident on some potential barrier

from math import sqrt

hBar = 1.05457E-34
eMass = 9.11E-31
E = 10
V = 9

k1 = (sqrt(2*eMass*E))/hBar
k2 = (sqrt(2*eMass*(E-V)))/hBar

T = (4*k1*k2)/(k1+k2)**2
R = ((k1-k2)/(k1+k2))**2

print("The probability of the particle to transmit (T) across the barrier V is ", T*100, "% and the probability for the particle to reflect (R) is ", R*100,"%")
