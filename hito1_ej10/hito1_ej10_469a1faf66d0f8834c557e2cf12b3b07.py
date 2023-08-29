usuario  = int(input("Ingrese el numero del usuario: "))
user = 10334151
contrasenia  = int(input("Ingrese la contraseña: "))
contra = 1803
cont = True
validar = True
contador = 0
cajero= 1000000
cuenta= 100000
continuar = True
Fin = True
while(validar == True and Fin == True):    
    while(usuario == 10334151 and contrasenia == 1803 and continuar == True):

        giro = int(input("ingrese el monto que desea girar: "))
        while ( ((giro <= cuenta) <= cajero) and contrasenia == 1803):
            cuenta = cuenta - giro
            cajero = cajero - giro
            print("sueldo cuenta=", cuenta)
            print("sueldo cajero= ", cajero)
            break  

    if continuar == False:
        Fin = False
        break
    print("clave invalida")        

    usuario  = int(input("Ingrese el numero del usuario: "))
    contrasenia  = int(input("Ingrese la contraseña: "))
    contador = contador + 1
    if(contador == 3):
        print("tarjeta bloqueada")
        validar = False
    
