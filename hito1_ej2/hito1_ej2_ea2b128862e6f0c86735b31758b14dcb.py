#Contestador de celular
nt  = int(input("Ingrese el numero telefonico: "))
hll = int(input("Ingrese la hora de llamada: "))

nt1=str(nt)
nt2= nt1[5:8]
nt3= int(nt2)

nt4=str(nt)
nt5=nt4[0:3]
nt6=int(nt5)

if(hll==0)or(hll==1)or(hll==2)or(hll==3)or(hll==4)or(hll==5)or(hll==6)or(hll==7):
    print("CONTESTAR")

elif(nt3==909)and(hll<14):
    print("CONTESTAR")

elif(hll==17)or(hll==18)or(hll==19)and(nt6==807):
    print("NO CONTESTAR")

else:
    print("NO CONTESTAR")