#Contestador de celular
numero=int(input("ingrese un numero telefonico:"))
hora=int(input("ingrese la hora de su llamada:"))
numero_srt=str(numero)
a=numero_srt[0:3]
print("los primeros numeros son:",a)
b=numero_srt[5:8]
print("los ultimos numeros son:",b)
c=877
c=str(c)
print("variable de comienzo",c)
d=909
d=str(d)
print("variable de termino")
if 0<=hora<=7:
    print("contestar")
elif 7<hora<14:
    if b==d:
        print("contestar")
    else:
        print("no contestar")
elif 14<=hora<17:
    print("no contestar")
elif 17<=hora<=19:
    if a==c:
        print("no contestar")
    else:
        print("contestar")
elif hora>19:
    print("no contestar")