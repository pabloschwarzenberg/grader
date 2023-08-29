#Sistema de Ecuaciones
import sys

txt =input("numero 1: ")
a= float(txt)
txt =input("numero 2: ")
b= float(txt)
txt =input("numero 3: ")
c= float(txt)
txt =input("numero 4: ")
d= float(txt)

txt =input("numero 5: ")
e= float(txt)
txt =input("numero 6: ")
f= float(txt)

det= a*e - b*d
if det!=0:
    x=(e*c-b*f)/det
    y=(a*f-d*c)/det


s_x= x/det
s_y= y/det

print("x=",s_x)
print("y=",s_y)