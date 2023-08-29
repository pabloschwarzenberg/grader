numero=input("ingrese numero telefonico: ")
z=list(map(int, str(numero)))
x=str(numero)
if len(z)==8:
  hora=int(input("ingrese hora de la llamada: "))
  if 0<=hora and hora<=23:
    if 0<=hora and hora<=7:
      print("Resultado: CONTESTAR")
    elif 8<=hora and hora<=14:
      if "909" in x:
        print("Resultado: CONTESTAR")
      else:
        print("Resultado: NO CONTESTAR")
    elif 17<=hora and hora<19:
      if "877" in x:
          print("Resultado: NO CONTESTAR")
      else:
          print("Resultado: CONTESTAR")
    elif 19<=hora and hora<=23:
      print("Resultado: NO CONTESTAR")

        