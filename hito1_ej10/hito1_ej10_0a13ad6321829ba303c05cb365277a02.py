cajero= 1000000
cuenta= 100000 
intentos= 0
ingreso="clave invalida"

while intentos<3 and ingreso=="clave invalida":
    usuario=int(input("Ingrese su usuario"))
    clave=int(input("Ingrese su clave"))
    
    if usuario==10334151 and clave==1803:
        ingreso="clave valida"
                  
        
    intentos=intentos+1

while ingreso=="clave valida" and intentos<3:
    opcion=input("elija opcion 1)retirar dinero 2)salir")
    if opcion=="1":
        monto=int(input("monto a retirar"))
        if monto > cuenta:
            print("Monto no permitido")
            
        else:
          cuenta= cuenta-monto
          cajero= cajero -monto
          print("Saldo cuenta : ", cuenta)
          print("Saldo cajero : ", cajero)
           
    if opcion=="2":
        break
           
     
if ingreso=="clave invalida":
   print("Cuenta bloqueada")