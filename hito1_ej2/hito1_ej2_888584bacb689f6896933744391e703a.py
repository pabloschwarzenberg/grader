#Contestador de celular
numero = input("Ingrese numero telefonico: ")
hora = int(input("Ingrese la hora de la llamada: "))
numero_lista = []
for letra in numero:
    numero_lista.append(letra)

if hora > 7 and hora < 15:
    if numero_lista[5] == "9" and numero_lista[6] == "0" and numero_lista[7] == "9":
        print("CONTESTAR")
    elif numero_lista[5] != "9" or numero_lista[6] != "0" or numero_lista[7] != "9":
        print("NO CONTESTAR")

if hora >= 17 and hora < 20:
    if numero_lista[0] == 8:
        if numero_lista[1] == 7:
            if numero_lista[2] == 7:
                print("CONTESTAR")
    if numero_lista[0] != 8:
        if numero_lista[1] != 7:
            if numero_lista[2] != 7:
                print("NO CONTESTAR")

if hora >= 0 and hora < 8:
    print("CONTESTAR")

if hora > 19:
    print("NO CONTESTAR")

print(numero_lista[0])
print(numero_lista[1])
print(numero_lista[2])     