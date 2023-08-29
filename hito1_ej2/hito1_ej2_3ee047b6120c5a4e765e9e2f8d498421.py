#Contestador de celular
num=int(input("Numero de Telefono: "))
hor=int(input("Hora de llamda: "))

if hor>=0 and hor<=7 :
    print("Contestar")

elif hor<=14 and hor>7 and ((num%1000)==909):
    print("Contestar")

elif hor<=14 and hor>7:
    print("Contestar")

elif hor>14 and hor<17:
    print("No contestar")

elif hor>=17 and hor<=19 and (num//100000)==877:
    print("No contestar")

elif hor>=17 and hor<=19 :
    print("Contestar")

elif hor>19 and hor<=24 :
    print("No Contestar")     