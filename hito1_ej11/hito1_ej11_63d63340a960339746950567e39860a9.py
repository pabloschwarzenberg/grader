#Cajero Automático
saldo = 1000000
billete_20 = 20 #400.000
billete_10 = 40 #400.000
billete_5 = 40  #200.000

#retiro maximo
cuenta=100000


#entradas
usuario = int(input("ingrese su usuario: "))
clave = int(input("ingrese su clave: "))

cajero=1000000


fallos = 0
i=0

while fallos<3 and i<1 :
    if clave != 1803:
        print("clave invalida")
        fallos +=1
        if fallos==3:
            print("tarjeta bloqueada")
        else:
            clave = int(input("ingrese su clave: "))
    else:
        monto = int(input("ingrese su monto: "))
        if monto<=100000:
            if monto%5000==0:
                print("saldo cuenta=",cuenta-monto)
                print("saldo cajero=",cajero-monto)
                montos5= []
                montos10 = []
                montos20 = []
                while monto!=0:
                    if monto%20==10000 or monto%20==0:
                        saldo = monto//20000
                        montos20.append(saldo)
                        monto = monto%20000
                        
                        if monto%10 == 5000 or monto%10 == 0:
                            saldo = monto//10000
                            montos10.append(saldo)
                            monto = monto%10000
                            
                            if monto%5 ==0:
                                saldo = monto//5000
                                montos5.append(saldo)
                                monto = monto%5000
                                

                print("billetes 20000={}\nbilletes 10000={}\nbilletes 5000= {}".format(sum(montos20),sum(montos10),sum(montos5)))
                """entero = monto//20000
                resto"""
                i += 1
            else:
                print("monto no permitido\nPor favor ingrese un nuevo monto de multiplo de 5000")
            
        else:
            print("monto no permitido")

    