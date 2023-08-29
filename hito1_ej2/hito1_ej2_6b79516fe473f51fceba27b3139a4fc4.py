#Contestador de celular
#Pedir Variables
nt = input("Ingrese numero telefonico:")
h = int(input("Ingrese la hora de la llamada"))
numero_lista = []
for letra in nt:
    numero_lista.append(letra)
if (h > 7 and h < 15):
    if numero_lista[5] == "9" and numero_lista[6] == "0" and numero_lista[7] == "9":
        print("CONTESTAR")
    elif numero_lista[5] != "9" or numero_lista[6] != "0" or numero_lista[7] != "9":
        print("NO CONTESTAR")
if (h >= 17 and h < 20):
    if numero_lista[0] == 8:
        if numero_lista[1] == 7:
            if numero_lista[2] == 7:
                print("CONTESTAR")
    if numero_lista[0] != 8:
        if numero_lista[1] != 7:
            if numero_lista[2] != 7:
                print("NO CONTESTAR")
if (h >= 0 and h < 8):
    print("CONTESTAR")
if (h > 19):
    print("NO CONTESTAR")
print(numero_lista[0])
print(numero_lista[1])
print(numero_lista[2])
      