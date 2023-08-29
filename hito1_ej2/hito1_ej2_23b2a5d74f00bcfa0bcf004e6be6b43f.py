#Contestador de celular
telefono = list(input("Ingrese numero telefonico: "))
hora = int(input("Ingrese hora de la llamada: "))
ex1 = ['9','0','9']
ex2 = ['8','7','7']

ultimos = telefono[5:8]
primeros = telefono[0:3]

num = "".join(ultimos)

print(ultimos)
print(telefono)
print(num)


if (hora > 0 and hora < 7):
    print("CONTESTAR")

elif (hora >= 7 and hora <= 14): 
    if set(ultimos) == set(ex1):
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
    
elif (hora >= 17 and hora <= 19):
    if set(primeros) == set(ex2):
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
else:
    if hora > 19:
        print("NO CONTESTAR")
    