#Contestador de celular
numero = int(input('Ingrese su número de celular: '))
hora = int(input('Ingrese la hora en que recibió la llamada: '))
numero=str(numero)
X=numero[5:8]
Y=numero[0:3]
print("vector",X)
print("vector",Y)
B=909
B=str(B)
C=877
C=str(C)
if 7 <= hora <= 14:
    if numero[5:8] == B:
        print("vector termino 909",numero[5:8])
        print('CONTESTAR')
    else:
        print('NO CONTESTAR')
else:
    if 17 <= hora <= 19:
        if numero[0:3] == C:
            print("vector else inicio 877",numero[0:3])
            print('NO CONTESTAR')
        else:
            print("CONTESTA")

    else:
        print("NO CONTESTAR")