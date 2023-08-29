#Contestador de celular
numero = int(input('Ingrese tu número de celular: '))
hora = int(input('Ingrese la hora de la llamada: '))
numero=str(numero)
X=numero[5:8]
Y=numero[0:3]
print("vector",X)
print("vector",Y)
ex=909
ex=str(ex)
ex_1=877
ex_1=str(ex_1)
if 7 <= hora <= 14:
    if numero[5:8] == ex:
        print("termino con 909",numero[5:8])
        print('CONTESTAR')
    else:
        print('NO CONTESTAR')
else:
    if 17 <= hora <= 19:
        if numero[0:3] == ex_1:
            print("inicio con 877",numero[0:3])
            print('NO CONTESTAR')
        else:
            print("CONTESTA")
                
if 19 < hora:
    print("NO CONTESTAR")
    
        






