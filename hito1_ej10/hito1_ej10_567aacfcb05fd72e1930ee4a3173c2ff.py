#Cajero Automático

SaldoCajero = 1000000
Usuario = int(input("Ingrese su usuario: "))
Clave = int(input("Ingrese su Clave: "))
PlataUsuario = 100000
ClaveFinal = 0
Intentos = 1

while (Usuario != 10334151 and Clave != 1803):
    if (Usuario != 10334151):
        Usuario = int(input("Ingrese su usuario: "))
    elif (Clave != 1803):
        Clave = int(input("Ingrese su Clave: "))

print("Usted tiene "+str(PlataUsuario), "en su banco")
Retiro = int(input("Cuánto dinero desea retirar: "))

while (PlataUsuario < Retiro or Retiro < 0):
    Retiro = int(input("Cuánto dinero desea retirar: "))
    
ClaveFinal = int(input("Ingrese su clave nuevamente: "))
while (ClaveFinal < 0):
  ClaveFinal = int(input("Ingrese su clave nuevamente: "))
  
while (Retiro < PlataUsuario and Intentos != 3):
    if (ClaveFinal != Clave):
        Intentos = Intentos + 1
        print("Esa no es su clave")
        ClaveFinal = int(input("Ingrese su clave nuevamente: "))
                        
    elif (ClaveFinal == Clave):
        SaldoCajero = SaldoCajero - Retiro
        PlataUsuario = PlataUsuario - Retiro
            
        print("Usted ha retirado el dinero correctamente")
        print("Saldo cuenta="+str(PlataUsuario))
        print("saldo cajero="+str(SaldoCajero))
        break
            
    elif (Intentos == 3 and ClaveFinal != Clave):
        print("Tarjeta Bloqueada")
        break