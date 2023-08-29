#Contestador de celular
num=int(input())
hora=int(input())

a=num//100000
b=num%1000

if(0<hora<=7):
    print("CONTESTAR")
elif(7<hora<=14 and b==909):
    print("CONTESTAR")
elif(7<hora<=14):
    print("NO CONTESTAR")
elif(14<hora<17):
    print("NO CONTESTAR")
elif(17<=hora<=19 and a==877):
    print("NO CONTESTAR")
elif(17<=hora<=19):
    print("CONTESTAR")
elif(19<hora<=23):
    print("NO CONTESTAR")