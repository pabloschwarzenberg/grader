#Contestador de celular
numero = int(input("ingrese su numero: "))
hora = int(input("ingrese la hora: "))
resto = numero - 909
#12345678

if hora >= 0 and hora <= 7:
  print("CONTESTA")
elif hora > 7 and hora < 14:
    print("NO CONTESTA")
elif resto%1000 == 0:
  print("CONTESTA")
elif hora >= 17 and hora <= 19:
  print("CONTESTA")
elif numero[0,1,2] == 877:
  print("NO CONTESTA")
elif numero > 19 and numero < 23:
  print("NO CONTESTA")