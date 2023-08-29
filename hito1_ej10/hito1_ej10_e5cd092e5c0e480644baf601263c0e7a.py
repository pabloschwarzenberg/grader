#Cajero Automático
usuario = 10334151
contra = 1803 

dinero_usuario = 100000
dinero_cajero = 1000000

acum= 0

ingreso_usuario = int(input("Ingrese el usuario: "))
ingreso_contra = int(input("Ingrese su clave: "))
if ingreso_usuario != usuario or ingreso_contra != contra:
  acum = acum+1
  print("Datos ingresados no validos")
  ingreso_usuario1 = int(input("Ingrese el usuario: "))
  ingreso_contra1 = int(input("Ingrese su clave: "))
  if ingreso_usuario1 != usuario or ingreso_contra1 != contra:
    acum = acum + 1
    print("Datos ingresados no validos")
    ingreso_usuario2 = int(input("Ingrese el usuario: "))
    ingreso_contra2 = int(input("Ingrese su clave: "))
    if ingreso_usuario2 != usuario or ingreso_contra2 != contra:
        print("Cuenta Bloqueada")

if (ingreso_usuario == usuario and ingreso_contra == contra) or \
   (ingreso_usuario1 == usuario and ingreso_contra1 == contra) or \
   (dinero_usuario2 == usuario and ingreso_contra2 == contra):
  retiro = int(input("Cuanto desea retirar?: "))
  nuevo_monto_usuario = dinero_usuario - retiro
  nuevo_monto_cajero = dinero_cajero - retiro
  print("saldo cuenta=", nuevo_monto_usuario)
  print("saldo cajero=", nuevo_monto_cajero)
