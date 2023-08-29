#Sistema de Ecuaciones
a1=int(input(""))
b1=int(input(""))
c1=int(input(""))
a2=int(input(""))
b2=int(input(""))
c2=int(input(""))
A1B2= a1 * b2
A2B1= a2 * b1
C1B2= c1 * b2
C2B1= c2 * b1
A1C2= a1 * c2
A2C1= a2 * c1
Det_Sis= A1B2 - A2B1
Det_x= C1B2 - C2B1
Det_y= A1C2 - A2C1
x= Det_x / Det_Sis
y= Det_y / Det_Sis
round(y)
round(x)
print("x=",x)
print("y=",y)