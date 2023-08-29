#Descomponer un número
a=int(input("ingrese su numero:"))
mil= a / 1000
p= a % 1000
centena= p / 100
p= p % 100
decima= p / 10
u= p % 10
print("%i" % mil,"M+","%i" % centena,"C+","%i" % decima,"D+","%i" % u,"U")