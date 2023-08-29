#Contestador de celular
tel=int(input("Telefono: "))
hora=int(input("Hora: "))


nueve=tel%1000

if(hora>=0) and (hora<=7):
 print("CONTESTAR")

elif(hora<14) and (nueve!=909):
 print("NO CONTESTAR")
elif(hora<14):
 print("CONTESTAR")

elif(hora<17):
    print("NO CONTESTAR")

if(hora>=17) and(hora<=19)and(tel//100000!=877):
    print("CONTESTAR")
if(hora>=17) and(hora<=19)and(tel//100000==877):
    print("NO CONTESTAR")

if(hora>19):
    print("NO CONTESTAR")