#Contestador de celular
numero = int(input('Ingrese su número de celular: '))
hora = int(input('Ingrese la hora en que recibió la llamada: '))
numero=str(numero)
a=numero[5:8]
e=numero[0:3]
print("vector",a)
print("vector",e)
b=909
b=str(b)
c=877
c=str(c)
if 7 <= hora <= 14:
    if numero[5:8] == b:
        print("vextor termino 909",numero[5:8])
        print('CONTESTAR')
    else:
        print('NO CONTESTAR')