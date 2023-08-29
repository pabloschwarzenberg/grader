#Sistema de Ecuaciones

L=[int(input(":")),int(input(":")),int(input(":"))]
L2=[int(input(":")),int(input(":")),int(input(":"))]
det=(L[0]*L2[1])-(L2[0]*L[1])
x=(((L[2]*L2[1])-(L2[2]*L[1]))/det).__round__(1)
y=-(((L[2]*L2[0])-(L2[2]*L[0]))/det).__round__(1)
print("x={0}".format(x))
print("y={0}".format(y))     