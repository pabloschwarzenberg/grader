#Encabezado
print("Conversor a numero binario")

#Definir variables y solicitar informacion por teclado

num = int(input("Ingrese numero a convertir: "))

#Operaciones

orden = ""

while num > 0 :
    res = num%2
    num = num //2
    orden = str(res) + orden

print( "Resultado = " + str(orden))