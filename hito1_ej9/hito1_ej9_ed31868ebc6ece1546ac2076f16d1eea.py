#Sistema de Ecuaciones
l1=[int(input(":")),int(input(":")),int(input(":"))]
l2=[int(input(":")),int(input(":")),int(input(":"))]
det=(l1[0]*l2[1])-(l2[0]*l1[1])
x=(((l1[2]*l2[1])-(l2[2]*l1[1]))/det).__round__(1)
y=-(((l1[2]*l2[0])-(l2[2]*l1[0]))/det).__round__(1)
print("x={0}".format(x))
print("y={0}".format(y))