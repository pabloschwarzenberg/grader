#Cajero Automático
saldoCajero = 1000000
bi20=20
bi10=40
bi5=40

usuarioValido=10334151
claveValida=1803
saldoUsuario= 100000

usuario=int(input("Ingrese usuario: "))

while usuario != usuarioValido:
    usuario=int(input("Ingrese usuario nuevamente: "))

clave=int(input("Ingrese clave: "))         
intentos= 0

while clave != claveValida:
    intentos=intentos+1
    
    if intentos== 3:
        print("Tarjeta bloqueada")
        break
    clave=int(input("Clave inválida: "))


if intentos != 3:
    montoRetirado= int(input("Ingrese monto: "))
    if montoRetirado > saldoCajero or  montoRetirado > saldoUsuario:
        print("Monto no permitido")
    else:
        saldoCajero= saldoCajero - montoRetirado
        saldoUsuario= saldoUsuario - montoRetirado
        cont20=0
        cont10=0
        cont5=0
        while montoRetirado>0:
            if(montoRetirado >= 20000):
               cont20=cont20 + 1
               bi20=bi20-1
               montoRetirado=montoRetirado-20000
            if(montoRetirado >= 10000):
               cont10=cont10 + 1
               bi10=bi10-1
               montoRetirado=montoRetirado-10000        
            if(montoRetirado >= 5000):
               cont5=cont5 + 1
               bi5=bi5-1
               montoRetirado=montoRetirado-5000  
        

        print("saldo cuenta=",saldoUsuario)
        print("saldo cajero=",saldoCajero)
        print("billetes 20000= ",cont20)
        print("billetes 10000= ",cont10)
        print("billetes 5000= ",cont5)

    
        
