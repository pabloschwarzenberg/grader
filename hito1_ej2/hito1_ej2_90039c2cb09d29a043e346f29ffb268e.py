#Contestador de celular
Numero=int(input())
Hora=int(input())

if 0<=Hora<=7:
    print("CONTESTAR")
elif 7<Hora<14 and (Numero-909)%1000!=0:
    print("NO CONTESTAR")
elif 7<Hora<14 and (Numero-909)%1000==0:
    print("CONTESTAR")
elif 14<=Hora<17:
    print("NO CONTESTAR")
elif 17<=Hora<=19 and (Numero-877)%1000!=0:
    print("NO CONTESTAR")
elif 17<=Hora<=19 and (Numero-877)%1000==0:
    print("CONTESTAR")
else:
    print("NO CONTESTAR")
        
  
