#Contestador de celular
celular=int(input("Ingrese un n° de 8 digitos por favor: "))
hora=float(input("Ingrese hora de la llamada, entre 00 y 23 hrs.: "))
resto = celular % 1000
celular = int(celular / 1000)
print("3 últimos dígitos",resto)
inicio=celular//100
print("3 primeros dígitos",inicio)
if 7<=hora<=00:
  print("CONTESTAR")
if hora<14 and resto!=909:
  print("NO CONTESTAR")
if resto==909 and hora<14:
    print("CONTESTAR")
if 17<=hora<=19:
  print("CONTESTAR")
  if inicio==877:
    print("NO CONTESTAR")
if hora>19:
  print("NO CONTESTAR")