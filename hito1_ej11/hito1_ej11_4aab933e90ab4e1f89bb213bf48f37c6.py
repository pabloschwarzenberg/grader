cajero = 1000000
usuario = 10334151
clave = 1803
contador = 0
usuariocuenta = 100000
intento = eval(input("su clave:"))
while intento != clave and contador != 2:
    print("clave invalida")
    intento = eval(input("su clave:"))
    contador +=1
    if contador ==2:
        print("tarjeta bloqueada")
else:
    if intento == clave:
        cuentaa = eval(input("cual es el monto a retirar?"))
        if 100000>=cuentaa>0:
            print("saldo cuenta=",100000-cuentaa)
            print("saldo cajero=",1000000-cuentaa)
            pesoschile=[5000,10000,20000]
            cambio=[0,0,0]
            resto=cuentaa
            contador=2

            while(resto!=0):
              if((resto-pesoschile[contador])>=0):
                cambio[contador]+=1
                resto-=pesoschile[contador]
              else:
                contador-=1
                if(contador<0):
                  break
            contador=2
            while(contador!=-1):
                print("billetes",pesoschile[contador],end = '=')
                print(cambio[contador])
                contador-=1


        else:
            print("monto no permitido")
