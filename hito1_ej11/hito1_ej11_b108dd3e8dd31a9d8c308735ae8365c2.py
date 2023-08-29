#Cajero Automático
y=int(input('ingrese nombre de usuario:'))
z=int(input('ingrese clave:'))
contador=1
saldo_c=1000000
saldo_p=100000
a=20000
b=10000
c=5000
d=1000
while contador <= 3:
    if y==10334151 and z== 1803:
        x=int(input('ingrese monto a retirar:'))
        if x>=100000:
            print('monto no permitido')
        else:
           
            def cajero(n):
                a1=0
                b1=0
                c1=0
                d1=0
                #el saldo de 1.000.000 estará distribuido en 20 billetes de 20.000, 40 billetes de 10.000 y 40 billetes de 5.000.
                a2= 20
                b2= 40
                c2=40
                while n>0:
                    if n>=20000:
                        n= n-a
                        a1+=1
                        a2-=1
            
                    elif n>=10000:
                        n= n-b
                        b1+=1
                        b2-=1
                    elif n>=5000:
                        n= n-c
                        c1+=1
                        c2-=1
            
                    elif n>=1000:
                        n= n-d
                        d1+=1
                #print('la suma de billetes es:', x)
                if a1>=1:
                    print('billetes 20000=',a1)
                if b1>=1:
                    print('billetes 10000=',b1)
                if c1>=1:
                    print('billetes 5000=',c1)
                if d1>=1:
                    print('billetes 1000=',d1)
                 
                print('saldo cuenta=', saldo_p-x)
                print('saldo cajero=', saldo_c-x)
                #print('billetes 20000=',a2)
                #print('billetes 10000=',b2)
                #print('billetes 5000=',c2)

            f=cajero(x)
            #print('saldo cuenta=', saldo_p-x)
           
            
            
            break
    else:
        if contador==3:
            print('targeta bloqueada')
            break
        else:
            print('clave invalida')
            z=int(input('ingrese clave:'))
            contador+=1
