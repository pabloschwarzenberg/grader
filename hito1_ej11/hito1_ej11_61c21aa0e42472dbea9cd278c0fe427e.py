#Cajero Automático
a = 20000 
b = 10000 
c = 5000  
saldo_cajero_inicial = 20*a + 40*b + 40*c
saldo_cuenta_inicial = 100000
intentos = 3
Y = True
N = False
while intentos >= 1:
    usuario = int (input ("Ingrese Usuario: "))
    clave = int (input ("Ingrese Clave: "))
    if clave == 1803 and usuario == 10334151 :
        monto_a_retirar = int (input ("Ingrese Monto a Retirar: "))
        saldo_cuenta = saldo_cuenta_inicial - monto_a_retirar
        saldo_cajero = saldo_cajero_inicial - monto_a_retirar
        if monto_a_retirar <= 100000:
            print("saldo cuenta= ",saldo_cuenta)
            print("saldo cajero= ",saldo_cajero)
            if monto_a_retirar % a == 0:
                print("billetes 20000=",int(monto_a_retirar / a))
            elif monto_a_retirar % b == 0:
                print("billetes 10000=",int(monto_a_retirar / b))
            elif monto_a_retirar % c == 0:
                print("billetes 5000=",int(monto_a_retirar / c))
            decision = input ("¿Desea Continuar? : ")
            if decision == True:
                continue
            else:
                break
                
        else:
            print("monto no permitido")
    else:
            print("clave invalida")
            intentos = intentos - 1
            if intentos == 0:
                print("tarjeta bloqueada")
                
      
