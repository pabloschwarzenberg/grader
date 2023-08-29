# Ingresamos el numero y la clave para el usuario
usuario1 = 10334151
clave1 = 1803

#saldo que tiene la persona
saldo = 100000
#saldo del cajero automatico
saldo_auto = 1000000



#VERIFICADOR DE USUARIO Y CONTRASEÑA 
contador = 1
while contador <= 3:
    usuario = int(input("Ingresa el Usuario: "))
    clave = int(input("Ingresa la clave: "))

#SI EL USUARIO Y LA CONTRASEÑA FUERON UN EXITO
    if ((usuario == usuario1) and (clave == clave1)):
     contador = 4
    else:

     print("clave invalida")
    if (contador == 3):
        
        print("tarjeta bloqueada")
        break
    contador = contador +1

else:

          print("100.000")
          dinero_retiro = int(input("Cuanto dinero deseas retirar: "))

          if((dinero_retiro > 100000) or (dinero_retiro < 0)):
           print("monto no permitido")

          else:
              if((dinero_retiro <= 100000) or (dinero_retiro == 0)):
               print()

resultado1= saldo - dinero_retiro
resultado2= saldo_auto - dinero_retiro

print("saldo cuenta=",resultado1, "," "saldo cajero=",resultado2)      