'''
Ahora tu cajero, además de hacer todo lo que debería hacer en el nivel 1, 
debe distribuir el monto a retirar entre los diferentes billetes que tiene disponibles, 
para ello al principio el saldo de 1.000.000 estará distribuido en 20 billetes de 20.000, 
40 billetes de 10.000 y 40 billetes de 5.000. Cuando se haga un giro tu cajero además de 
imprimir los saldos, debe imprimir la cantidad de billetes que le entrega a la persona, 
por ejemplo al retirar 45.000 podría imprimir:

billetes 20000=1
billetes 10000=3
billetes 5000=1

Puedes distribuir los billetes de otra forma, lo importante es que la distribución 
cuadre con el monto solicitado.
'''
saldoCajero=1000000
saldoCuenta=100000
cuenta=int(input())
clave=int(input())
valor=int(input())
_20k=0
_10k=0
_5k=0
while valor > 1000:
    if valor > 20000:
        _20k+=1
        valor-=20000
        saldoCajero-=20000
        saldoCuenta-=20000
    elif valor > 10000:
        _10k+=1
        valor-=10000
        saldoCajero-=10000
        saldoCuenta-=10000
    elif valor > 1000:
        _5k+=1
        valor-=1000
        saldoCajero-=1000
        saldoCuenta-=1000
print('saldo cuenta=',saldoCuenta,'saldo cajero=',saldoCajero)
print('billetes 20000=',_20k)
print('billetes 10000=',_10k)
print('billetes 5000=',_5k)