#Contestador de celular
a=int(input())#Número
b=int(input())#Hora

if 0>b>7:
    print("CONTESTAR")
elif (7<b<14) and (a%1000==909):
    print("CONTESTAR")
elif (7<b<14) and not(a%1000==909):
    print("NO CONTESTAR")
elif (17<b<19) and (a//10000):
    print("NO CONTESTAR")
elif (17<b<19) and not(a//10000):
    print("CONTESTAR")
elif (19<b<24):
    print("NO CONTESTAR")
else:
    print("CONTESTAR")      