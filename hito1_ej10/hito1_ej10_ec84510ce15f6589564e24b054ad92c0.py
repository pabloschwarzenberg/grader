#Cajero Automático
rut=10334151
clave=1803
intento=0
monto=500000
print("Ingrese Rut")
Rut = int(input("Rut: "))
while Rut!=10334151:
    Rut=int(input("Rut incorrecto, Intente nuevamente: "))     
clave=int(input("Ingrese su clave: "))     
while clave!=1803:
    clave=int(input("Ingrese su clave nuevamente: "))
    intento=intento+1
    if intento==2:
        print("Tarjeta Bloqueada, gracias por su preferencia")
        break
else:
 print("Bienvenido al Banco X")
monto=int(input("Su saldo actual es de $1000000,Cuanto desea retirar: "))
while monto!=500000:
    monto=str(input("La cantidad ingresada no es valida, ingrese un multiplo de $500.000: "))
    intento=intento+1
    if intento==2:
       print("El multiplo ingresado no es el correcto, hasta luego")
       break
        
else:
    print("Un momento porfavor...")
    print("Su saldo actual es de $500.000")
    print("Gracias por operar con nosotros, hasta la proxima")      