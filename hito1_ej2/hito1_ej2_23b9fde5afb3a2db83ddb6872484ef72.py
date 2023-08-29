#Contestador de celular
#Ingreso telefono
nt = input("Ingrese un número telefonico: ")
while len(nt) > 8 or len(nt) < 8 :
   n_telefonico = input("Ingrese un número telefonico de 8 digitos: ")

#Ingreso hora
hora = input("Ingrese hora de llamada: ") 
if hora[0]=="0":
  hora = eval(hora[1])
else:
  hora = eval(hora)

#Analisis datos:
if hora < 14 and hora > 7:
  if nt[5]==nt[7]=="9" and nt[6]=="0":
    print("CONTESTAR")
  else:
    print("NO CONTESTAR")
elif hora < 20 and hora > 16:
  if nt[1]==nt[2]=="7" and nt[0]=="8":
    print("NO CONTESTAR")
  else:
    print("CONTESTAR")
elif hora > 18:
  print("NO CONTESTAR")
else:
  print("CONTESTAR")