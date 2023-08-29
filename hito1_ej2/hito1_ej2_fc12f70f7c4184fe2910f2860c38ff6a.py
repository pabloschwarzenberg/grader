#Contestador de celular
numero = int(input("Ingrese un número de celular (8 cifras): "))
hora = int(input("Ingrese la hora en que recibió la llamada: "))
numero=str(numero)
a=numero[5:8]
e=numero[0:3]
t=909
t=str(t)
c=877
c=str(c)
if 0<=hora<=7:
    print("CONTESTAR")
elif hora<14 and numero[5:8]==t:
    print("CONTESTAR")
elif hora<14:
    print("NO CONTESTAR")    
elif 17<=hora<=19 and numero[0:3]==c:
    print("NO CONTESTAR")
elif 17<=hora<=19:
    print("CONTESTAR")    
else:
    print("NO CONTESTAR")