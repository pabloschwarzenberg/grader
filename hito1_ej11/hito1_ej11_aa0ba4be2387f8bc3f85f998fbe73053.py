#Cajero Automático
salcaj=1000000
salcu=100000
fr=True
numve=0

bil20=20000
bil10=10000
bil5=5000

bill20=(bil20*2)/1000
bill10=(bil10*4)/1000
bill5=(bil5*8)/1000


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

gen=True
if(fr==True):

    while(fr==True):
        reti1=str(input(""))
        reti=int(reti1)
        nsalcaj=salcaj-reti
        nsalcu=salcu-reti
        if(reti<=salcaj):
            while(gen==True):
                if(reti<=salcu):
                    print("el saldo disponible del cajero es:",nsalcaj,"\nel saldo disponible da la cuenta es:",nsalcu)
                    print("BILLETES 20000=",bill20)
                    print("BILLETES 10000=",(salcu-reti)/1000)
                    print("BILLETES 5000=",bill5)
                    break
                else:
                    print("saldo de la cuenta insuficiente\nintente nuevamente")
                    gen=True
        else:
            print("saldo insuficiente para retirar ese monto\nintente nuevamente")
            fr=True