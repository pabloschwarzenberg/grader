print("Llamando...")
Num=int(input("Número Telefonico: "))
Hora=int(input("Hora de Llamada (formato 24 hrs): "))
Digitos = int (Num % 1000)
Digitos2 = int (Num / 100000)

if Hora < 7 and Hora >0:
    print("contestar")
elif Hora < 14 and Hora > 7 and Digitos ==909 :
    print("contestar")
elif Hora < 19 and Hora > 17 and Digitos2 !=877 :
    print(" Contestar")
elif Digitos2 == 877:
    print("No Contestar")
elif Hora >19 and Hora < 24 :
    print("No contestar")