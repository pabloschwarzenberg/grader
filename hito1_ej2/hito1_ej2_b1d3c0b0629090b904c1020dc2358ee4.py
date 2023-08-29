#Contestador de celular
numero = (input("Ingrese numero telefonico:"))
hora = int(input("Ingrese hora de la llamada:"))

#variable para definir si se contesta o no (1)No contesta (2)Contesta
resultado = 1
#variable para definir los ulimos 3 digitos del numero
ultimos = (numero[5:8])
#variable para definir los primeros 3 digitos del numero
primeros = (numero[0:3])


if 0 >= hora <= 7 :
    resultado = resultado + 1
 
elif hora > 19 : 
    resultado = resultado + 0

elif hora < 14 :
    resultado = resultado + 0
    if ultimos == "909":
        resultado = resultado + 1

elif 17 <= hora >=  19 :
    resultado = resultado + 1
    if primeros == "877" :
        resultado = resultado - 1
        
if resultado == 2 :
    print("Resultado: CONTESTAR")
elif resultado == 1:
    print("Resultado: NO CONTESTAR")      