#Benjamín Araya
print("Ingrese a continuacion su número teléfonico y la hora de llamada")
numero=int(input("Número teléfonico:"))
print("La Hora se escribe en enteros entre 0 y 23")
hora=int(input("Hora de llamada:"))
calculo=numero/1000
boing=str(calculo).split(".")
join=int(boing[1])
if(numero<10000000)or(numero>99999999):
  print("Numero completamente invalido")
else:
  if(hora>=0 and hora<=7):
    print("CONTESTAR")
  else:
    if(hora>19 and hora<24):
      print("NO CONTESTAR")
    else:
      if(hora>23):
        print("HORA INEXISTENTE, INGRESE UNA REAL")
      else:
        if(hora>=17 and hora<=19)and(numero>=87700000 and numero<=87799999):
          print("NO CONTESTAR")
        else:
          if(hora>7 and hora<14)and(join==909):
            print("CONTESTAR")
          else:
            if(hora>7 and hora<14):
              print("NO CONTESTAR")
            else:
              print("CONTESTANDO")

