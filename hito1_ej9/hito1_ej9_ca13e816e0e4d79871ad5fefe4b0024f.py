#Sistema de Ecuaciones
a=[int(input(":")),int(input(":")),int(input(":"))]
b=[int(input(":")),int(input(":")),int(input(":"))]
det=(a[0]*b[1])-(b[0]*a[1])
x=(((a[2]*b[1])-(b[2]*a[1]))/det).__round__(1)
y=-(((a[2]*b[0])-(b[2]*a[0]))/det).__round__(1)
print("x={0}".format(x))
print("y={0}".format(y))