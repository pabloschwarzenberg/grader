#Contestador de celular
numero_telefonico=int(input())
a=numero_telefonico
hora_de_llamada=int(input())
b=hora_de_llamada
c=c=a-round(a//1000,0)*1000
d=a//100000
if 0<=b<=7:
    print("Contestar")
if 7<b<=14 and not(c==909):
    print("No Contestar")
if 7<b<=14 and(c==909):
    print("Contestar")
if 14<b<17:
    print("No contestar")
if 17<=b<19 and not(d==877):
    print("Contestar")
if 17<=b<19 and(d==877):
    print("No contestar")
if 19<=b<=23:
    print("No contestar")