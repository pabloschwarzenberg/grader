#Contestador de celular
numero=input("numero telefonico")
hora=int(input("hora de la llamada"))
t=int(numero[5]+numero[6]+numero[7])
p=int(numero[0]+numero[1]+numero[2])
if 0<=hora<=7:
  print("CONTESTAR")
elif 7<hora<=14 and t==909:
    print("CONTESTAR")
elif 17<=hora<=19 and p!=877:
    print("CONTESTAR")
else:
    print("NO CONTESTAR")