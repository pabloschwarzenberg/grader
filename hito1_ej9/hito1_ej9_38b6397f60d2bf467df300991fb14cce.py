#Sistema de Ecuaciones
sistema1=[int(input(":")),int(input(":")),int(input(":"))]
sistema2=[int(input(":")),int(input(":")),int(input(":"))]
det=(sistema1[0]*sistema2[1])-(sistema2[0]*sistema1[1])
x=(((sistema1[2]*sistema2[1])-(sistema2[2]*sistema1[1]))/det).__round__(1)
y=-(((sistema1[2]*sistema2[0])-(sistema2[2]*sistema1[0]))/det).__round__(1)
print("x={0}".format(x))
print("y={0}".format(y))
    