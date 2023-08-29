#Cajero automático


usuario_registrado= "10334151"
clave_registrada= "1803"
Saldo_cajero=1000000
Saldo_usuario=100000


def Validar(usuario,clave):
    if usuario!=usuario_registrado or clave!=clave_registrada:
        print("clave invalida")
        return False
        
    else:
        #print("Bienvenido")
        return True




#a=input("Ingrese su usuario: ")
#b=input("Ingrese su clave: ")

#Validar(a,b)



def Validar_monto(retiro):
    if retiro>Saldo_cajero or retiro>Saldo_usuario:
        #print("monto no permitido")
        return False
    else:
        #print("Good")
        return True


#a=2000000
#Validar_monto(a)

# ESTO DEBE IR DENTRO DE UN WHILE NOMBRE != "N"????

nombre_usuario=""
if nombre_usuario!="N":
    intentos=3
    while intentos>0:
        nombre_usuario=input("Ingrese su nombre de usuario: ")
        clave_usuario=input("Ingrese su clave: ")
        if Validar(nombre_usuario,clave_usuario)==False:
            intentos-=1
            
        else:
            print("Bienvenido")
            monto_retirar=int(input("Indique cuanto desea retirar: "))
            if Validar_monto(monto_retirar)==False:
                print("monto no permitido")
            else:
                Saldo_cajero-=monto_retirar
                Saldo_usuario-=monto_retirar
                print("saldo cuenta=",Saldo_usuario, "saldo cajero=",Saldo_cajero)
                                
            break
    if intentos==0:
       print("tarjeta bloqueda")
        
else:
    False

    