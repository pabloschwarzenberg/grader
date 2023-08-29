#Contestador de celular
numero = input("Ingrese número telefónico: ")
numero_lista = []
for elemento in numero: #Transformar valores string a int
    numero_lista.append(int(elemento))
while len(numero_lista) != 8: #Ciclo error si el número ingresado no tiene 8 dígitos
    numero = input("Ingrese número telefónico nuevamente que cuento con 8 dígitos: ")
    numero_lista = []
    for elemento in numero:
        numero_lista.append(int(elemento))

hora = int(input("Ingrese hora de la llamada: "))
while hora < 0 or hora > 23:
    hora = int(input("Ingrese hora de la llamada nuevamente: "))
else:
    if hora >= 0 and hora <= 7:
        print("Resultado: CONTESTAR")
    elif hora < 14 and numero_lista[-3] == 9 and numero_lista[-2] == 0 and numero_lista[-1] == 9:
        print("Resultado: CONTESTAR")
    elif hora < 14:
        print("Resultado: NO CONTESTAR")
    elif hora >= 17 and hora <= 19 and numero_lista[0] == 8 and numero_lista[1] == 7 and numero_lista[2] == 7:
        print("Resultado: NO CONTESTAR")
    elif hora >= 17 and hora <= 19:
        print("Resultado: CONTESTAR")
    else:
        print("Resultado: NO CONTESTAR")