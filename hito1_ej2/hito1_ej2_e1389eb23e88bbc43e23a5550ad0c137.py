#Contestador de celular
print("Ingrese numero telefonico de 8 cifras")
nt=int(input("numero telefonico="))
print("ingrese hora de llamada")
h=int(input("hora de llamada"))

if len(str(nt)) == 8:
  if (h>=0) and (h<=23):
    if (h>=0) and (h<=7):
      print("CONTESTAR")
    elif(h<=14):
      if nt%1000 == 909:
        print("CONTESTAR")
      else:
        print("NO CONTESTAR")
    elif (h>=17) and (h<=19):
      if nt//100000 == 877:
        print("NO CONTESTAR")
      else:
        print("CONTESTAR")
    elif (h>19) and (h<=23):
      print("NO CONTESTAR")
      