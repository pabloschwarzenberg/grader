#Contestador de celular
a=(input())
b=int(input())
if(0<=b<=7):
    print("CONTESTAR")
elif((7<b<=14)and(int(a[5:8:1])!=909)):
    print("NO CONTESTAR")
elif((7<b<=14)and(int(a[5:8:1])==909)):
    print("CONTESTAR")
elif((17<=b<=19)and(int(a[0:3:1])!=877)):
    print("CONTESTAR")
elif((17<=b<=19)and(int(a[0:3:1])==877)):
    print("NO CONTESTAR")
elif(14<b<17):
    print("NO CONTESTAR")
elif(19<b):
    print("NO CONTESTAR")