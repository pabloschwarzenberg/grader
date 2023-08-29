#Cajero Automático
saldo_inicial=1000000

intentos=3
while intentos>0:
    usuario= (input("Ingrese usuario:"))
    clave= int(input("Ingrese clave:"))
    
    saldo_cuenta= 100000
    if (usuario==10334151) and (clave==1803):
        print ("clave valida, Bienvenido")
        retiro= int(input("Ingrese monto a retirar:"))
        if (retiro<=saldo_cuenta):
            saldo_cuenta=  saldo_cuenta-retiro
            saldo_cajero=saldo_inicial-retiro
            print ("saldo cuenta:",saldo_cuenta) 
            print ("saldo cajero:",saldo_cajero)
    
        
    else:
      print ("clave invalida")
      intentos=intentos-1
      break
            