#Contestador de celular
numero=input()
hora=int(input())
if(hora>0)and(hora<=7)and(len(numero)==8):
  print("CONTESTAR")
elif(hora>=19):
  print("NO CONTESTAR")
else:
  contestar = "909"
  contestarnt="877"
  if(hora>7)and(hora<14)and(numero[-1] + numero[-2] + numero[-3] == contestar):
    print("CONTESTAR")
  elif(hora>=17)and(hora<=19)and(numero[0] + numero[1] + numero[2] == contestarnt):
    print("NO CONTESTAR")
  elif(hora>=17)and(hora<=19):
    print("CONTESTAR")
  else:
    print("NO CONTESTAR")