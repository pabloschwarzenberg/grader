#Contestador de celular
numero=int(input())
hora=int(input())
if((0<=hora and hora<=7) or hora==24 ):
    print("CONTESTAR")
elif((8<=hora and hora<=14) and numero%1000==909):
    print("CONTESTAR")
elif(17<=hora and hora<=19 and not(numero//100000==877)):
    print("CONTESTAR")
elif(19>=hora and hora<24):
    print("NO CONTESTAR")
else: 
    print("NO CONTESTAR")    