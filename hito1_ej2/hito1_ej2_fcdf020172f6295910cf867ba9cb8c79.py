#Contestar automaticamente el celular

numero = int(input("Ingrese el número telefónico: "))

while numero < 12345678 or numero > 99999999:
    print("\nNúmero telefónico inválido.")
    numero = int(input("Ingrese el número telefónico: "))

numero = str(numero)

hora = int(input("Ingrese hora de la llamada: "))

while hora <0 or hora >24:
    print("\nHora incorrecta.")
    hora = int(input("Ingrese hora de la llamada: "))


if hora > 0 and hora < 7:
    print("CONTESTAR")

elif hora > 7 and hora < 14 and str(numero[5]) == "9" and str(numero[6]) == "0" and str(numero[7]) == "9":

    print("CONTESTAR")

elif hora > 7 and hora < 14:

    print("NO CONTESTAR")

elif hora > 17 and hora < 19 and str(numero[0]) == "8" and str(numero[1]) == "7" and str(numero[2]) == "7":

    print(" NO CONTESTAR")

elif hora > 19:
    print("NO CONTESTAR")
     
      