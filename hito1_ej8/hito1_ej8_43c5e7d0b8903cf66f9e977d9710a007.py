#Descomponer un número
print("Ingresar un numero: ")
numero=int(input())

UnidadMil=numero / 1000
x=numero%1000

Centena=x/100
x=x%100

Decena=x/10
Unidad=x%10

print("%i" % UnidadMil, "M+", "%i" % Centena, "C+", "%i" % Decena, "D+", "%i" % Unidad, "U")
