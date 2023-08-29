#Contestador de celular
#Daniel Barrios
celular=int(input("Ingrese un n° de 8 digitos por favor: "))
hora=float(input("Ingrese hora de la llamada, entre 00 y 23 hrs.: "))
resto = celular % 1000
celular = int(celular / 1000)
print("3 últimos dígitos",resto)
inicio=celular//100
print("3 primeros dígitos",inicio)
if 0<=hora<=7:
  print("CONTESTAR")
else:
  if hora<=8<=14:
    print("NO CONTESTAR")
  else:
    if resto==909:
       print("CONTESTAR")
    else:
      if hora>=17<=19:
        print("NO CONTESTAR")
      else:
        if inicio==877:
          print("NO CONTESTAR")
        else:
          if hora>19:
            print("NO CONTESTAR")
            