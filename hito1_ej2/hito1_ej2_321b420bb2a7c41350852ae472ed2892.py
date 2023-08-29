#Contestador de celular

numero = int(input('Ingrese su número de celular: '))
hora = int(input('Ingrese la hora en que recibió la llamada: '))
numero_str = str(numero)

print("variable STR:", numero_str)
a=numero_str[0:3]
print("los pirmeros numeros son : " , a)
b=numero_str[5:8]
print("los ultimos numeros son :", b)
c=877
c=str(c)
print("variable de inicio 3 digitos:",c)
d=909
d=str(d)
print("variable de termino 3 digitos:",d)
if 0 <= hora <= 7:
    print('CONTESTAR')
elif 7<hora<14:
    if b==d:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif 14<=hora<17:
    print("CONTESTAR")
elif 17<=hora<=19:
    if a==c:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
elif hora>19:
    print("NO CONTESTAR")

