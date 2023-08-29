#Sistema de Ecuaciones
P=[int(input(":")),int(input(":")),int(input(":"))]
o=[int(input(":")),int(input(":")),int(input(":"))]
det=(p[0]*o[1])-(o[0]*p[1])
x=(((o[2]*p[1])-(o[2]*p[1]))/det).__round__(1)
y=-(((p[2]*o[0])-(o[2]*p[0]))/det).__round__(1)
print("x={0}".format(x))
print("y={0}".format(y))
      