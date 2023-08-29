#Contestador de celular
n = int(input('Ingrese su número de celular: '))
h = int(input('Ingrese la hora en que recibió la llamada: '))
n=str(n)
a=n[5:8]
e=n[0:3]
b=909
b=str(b)
c=877
c=str(c)
if 7 <= h <= 14:
    if n[5:8] == b:
        print("vector termino 909",n[5:8])
        print('CONTESTAR')
    else:
        print('NO CONTESTAR')
else:
    if 17 <= h <= 19:
        if n[0:3] == c:
            print("vector else inicio 877",n[0:3])
            print('NO CONTESTAR')
        else:
            print("CONTESTA")

    else:
        print("NO CONTESTAR")
