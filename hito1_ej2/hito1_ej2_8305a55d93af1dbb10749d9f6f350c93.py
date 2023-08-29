#Contestador de celular
n=int(input("Ingrese el numero :"))
h=int(input("Ingrese la hora :"))
x=n
inicio=x//100000
final=x%1000
if 0<=h<=7:
    print("Resultado: Contestar posible emergencia")
elif 7<h<=14 and final == 909:
    print("Resultado: Contestar")
elif 7<h<=14:
     print("Resultado: No Contestar")
elif 17<=h<=19:
    print("Resultado: No Contestar")
elif 17<=h<=19 and incio==877 :
    print("Resultado: Contestar")
elif 19<h:
    print("Resultado: No Contestar")
    