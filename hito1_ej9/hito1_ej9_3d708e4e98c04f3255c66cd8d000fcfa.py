from math import *

s1, s2 = [], []

s1.append(int(input()))
s1.append(int(input()))
s1.append(int(input()))
s2.append(int(input()))
s2.append(int(input()))
s2.append(int(input()))

str1 = str(s1[0]) + "x+" + str(s1[1]) + "y=" + str(s1[2])
str2 = str(s2[0]) + "x+" + str(s2[1]) + "y=" + str(s2[2])
print("Ecuación 1:", str1, "\nEcuación 2:", str2)

# ESQUEMA
# ec1 será -> s1[0]x + s1[1]y = s1[2]
# ec2 será -> s2[0]x + s2[1]y = s2[2]

resY = round(((s1[0]*s2[2])-(s2[0]*s1[2]))/((s1[0]*s2[1])-(s2[0]*s1[1])), 1)
resX = round((s1[2]-(s1[1]*resY))/s1[0], 1)

print("x=" + str(resX))
print("y=" + str(resY))