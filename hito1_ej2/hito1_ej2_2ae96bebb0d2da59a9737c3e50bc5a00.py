#Contestador de celular
numero = int(input())
hora = int(input())
respuesta = str(0)

if (hora>=0) and (hora<=7):
  print(CONTESTAR)
if hora<14:
  respuesta = 1>0
  if (respuesta == True) and (numero%1000==909):
    print("CONTESTAR")
  else:
    print("NO CONTESTAR")
if (hora>=17) and (hora<=19):
  respuesta = 1>0
  if (respuesta==True) and (numero//10000):
    print("NO CONTESTAR")
  else:
    print("CONTESTAR")
if hora>19:
  print("NO CONTESTAR")