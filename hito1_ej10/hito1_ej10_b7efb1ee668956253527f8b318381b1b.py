#Cajero Automático
saldo_c=1000000
saldo_u=100000
x='Y'
while x != 'N':
    i=0
    usuario = input("Ingrese usuario: ")
    if usuario=='N':
        x='N'
    else:
        while usuario =='10334151':
            if i == 3:
                print("Tarjeta bloqueada")
                break
            else:
                clave = input("Ingrese clave: ")
                if clave=='N':
                    x='N'
                else:
                    if clave != '1803':
                        print("clave invalida")
                        i=i+1    
                    else:
                        
                        while True:
                            print("¿Cuanto monto desea retirar?")
                            monto=int(input())
                            if monto=='N':
                                x='N'
                            else:
                                if monto > saldo_u or monto > saldo_c:
                                    print("monto no permitido")
                            
                                else:
                                    saldo_c = saldo_c -monto
                                    saldo_u =saldo_u-monto
                                    print("saldo cuenta=",saldo_u)
                                    print("saldo cajero=",saldo_c)
                                    break
                        break
      