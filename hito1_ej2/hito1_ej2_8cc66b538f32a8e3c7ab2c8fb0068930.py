#Contestador de celular

a=int(input("Número: "))
b=int(input("Hora: "))

if(0<=b<7):
    print("CONTESTAR")
elif((7<=b<14)and(a%1000==909)):
    print("CONTESTAR")
elif((17<=b<=19)and(a//100000!=877)):
    print("CONTESTAR")
else:
    print("NO CONTESTAR")