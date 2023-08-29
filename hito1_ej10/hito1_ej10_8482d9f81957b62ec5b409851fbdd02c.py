print("bienvenido al acumulador de dinero universal")

intento = 1


dinerocajero= 1000000
plata=100000
usuario = int(input("ingrese su numero de usuario: "))
clave = int(input("ingrese su clave: "))


    
while (usuario != 10334151 and clave != 1803):
    if(intento < 3):
        intento= intento + 1
        print("porfavor ingrese sus datos correctamente")
        usuario = int(input("ingrese su numero de usuario: "))
        clave = int(input("ingrese su clave: "))
        if (intento == 3):
            print("tarjeta bloqueada")
        
if(usuario == 10334151 and clave == 1803):

    retiro= int(input("su sueldo actual es de 100.000 pesos, cuanto dinero desea retirar? "))

    if(1000000 >= retiro):
        print ("saldo cuenta =", plata - retiro)
        print ("saldo cajero =", dinerocajero -retiro)



 



 
    
        
   