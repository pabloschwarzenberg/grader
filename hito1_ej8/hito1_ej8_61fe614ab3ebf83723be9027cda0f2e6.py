#Descomponer un número
numero=int(input("Introdusca un numero de a lo menos 4 digitos: "))
u_mil=numero / 1000
tmp=numero % 1000
centenas=tmp / 100
tmp=tmp % 100
decenas = tmp / 10
unidades = tmp % 10
print("Unidad de mil: %i" % u_mil)
print("Centenas: %i" % centenas)
print("Decenas: %i" % decenas)
print("Unidades: %i" % unidades)      