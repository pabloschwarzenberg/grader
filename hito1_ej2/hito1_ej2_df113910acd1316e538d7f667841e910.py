celular = str(input("Indique el número de teléfono (8 cifras): "))
hora = int(input("Indique la hora de la llamada: "))
n = len(str(celular))

if n!=8 or hora>23 or hora<0:
    celular = int(input("Ingrese numero telefonico válido:"))
    hora = input("Ingrese un a hora válida: ")

if hora>0 and hora<=7:
     print("CONTESTAR")
elif hora>19 and hora<=23:
 print("NO CONTESTAR")
else:
 if hora > 7 and hora < 14 and str(celular[-3])=="9" and str(celular[-2])=="0" and str(celular[-1])== "9":
  print("CONTESTAR")

 if hora > 7 and hora < 14 and str(celular[-3])!="9" and str(celular[-2])!="0" and str(celular[-1])!="9":
  print("NO CONTESTAR")

 if hora > 17 and hora < 19 and str(celular[0:1])=="8" and str(celular[1:2])=="7" and str(celular[2:3])=="7":
  print("NO CONTESTAR")
 
 if hora > 17 and hora < 19 and str(celular[0:1])!="8" and str(celular[1:2])!="7" and str(celular[2:3])!="7":
  print("CONTESTAR")