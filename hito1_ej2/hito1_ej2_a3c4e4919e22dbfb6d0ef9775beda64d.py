#introduzca automaticamente el celular

nroTel = int(input("Introduzca el número telefónico: "))

while nroTel < 12345678 or nroTel > 99999999:
    print("\nNúmero telefónico inválido.")
    nroTel = int(input("Introduzca el número telefónico: "))

nroTel = str(nroTel)

hora = int(input("Introduzca hora de la llamada: "))

while hora <0 or hora >24:
    print("\nHora incorrecta.")
    hora = int(input("Introduza hora de la llamada: "))


if hora >=0 and hora <= 7:
    print("CONTESTAR")

elif hora > 7 and hora < 14 and str(nroTel[5]) == "9" and str(nroTel[6]) == "0" and str(nroTel[7]) == "9":

    print("CONTESTAR")

elif hora > 7 and hora < 14:

    print("NO CONTESTAR")

elif hora > 17 and hora < 19 and str(nroTel[0]) == "8" and str(nroTel[1]) == "7" and str(nroTel[2]) == "7":

    print("NO CONTESTAR")

elif hora > 17 and hora < 19:
  
    print("CONTESTAR")

elif hora > 19:
    print("NO CONTESTAR")