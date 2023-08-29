#Cajero Automático
salcaj=1000000
salcu=100000
fr=True
numve=0
usu=str(input("ingrese su usuario porfavor: "))
while(fr==True):
    cla=str(input("ingrese su clave porfavor: "))
    numve=numve+1
    if(cla=='1803'):
        print("bienvenido")
        break
    else:
        if(numve<=3):
            numve=numve+1
            print("clave invalida\nintente nuevamente")
            fr=True
        else:
            print("tarjeta bloqueada")
            fr=False


if(fr==True):

    while(fr==True):
        reti=int(input("cuanto dinero desea retirar?: "))   
        nsalcaj=salcaj-reti
        nsalcu=salcu-reti
        if(reti<=salcaj):
            print("saldo cuenta=",nsalcu,"\nsaldo cajero=",nsalcaj)
            break
        else:
            print("saldo insuficiente para retirar ese monto\nintente nuevamente")
            fr=True
