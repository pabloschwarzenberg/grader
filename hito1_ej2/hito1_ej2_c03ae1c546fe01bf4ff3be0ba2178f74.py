#Contestador de celular
print("CONTESTADOR AUTOMATICO")
print("")
N=int(input("Numero de Telefono: "))
H=int(input("Hora de la llamada: "))
       
print("")
if H >= 0 and H <= 7:
      print("Contestar")
if H >= 8 and H <= 14:
      if (N-909)%100 == 0:
          print("Contestar")
      else:
          print("No contestar")
if H == 15 or H == 16:
    print("No contestar")
if H == 18 or H == 19 or H == 17:
    if N-87700000 >= 1 and N-87700000 <= 99999:
        print("No Contestar")
    else:
        print("Contestar")
if H >= 20 and H <= 23:
      print("No contestar")
if H > 23 or H < 0:
      print("Hora no valida")
