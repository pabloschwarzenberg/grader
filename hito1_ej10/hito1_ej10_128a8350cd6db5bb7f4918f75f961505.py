#Cajero Automático
usuarioEnBD = "10334151"
claveEnBD = "1803"
sesion = False
saldo = 100000
iniciar = True
def validarUsuario(usuario, clave) :
   global sesion
   if (usuario == usuarioEnBD and clave == claveEnBD) :
     sesion = True
     return True
   return False
def login() :
   global sesion
   if (sesion) :
     return True
   usuario = input("Digite usuario: ")
   clave = input("Digite contraseña: ")
   return validarUsuario(usuario, clave)
def retirar(valor) :
   global saldo
   if (valor > saldo) :
     return False, saldo
   saldo = saldo - valor
   return True, saldo
def accion(opcion) :
   if (opcion == 1) :
     valor = int(input("Digite el valor a retirar: "))
     return retirar(valor)
def ejecutar() :
   if not login() :
     print("usuario o contraseña inválido")
     return
   print("¿Qué desea hacer?")
   opcion = int(input("1 => Retirar: "))
print("Bienvenido")
while (iniciar == True) :
   ejecutar()
   respuesta = input("¿Deseas realizar otra operación? (SI => s, si y NO => valor diferete de s, si): ")
   if (respuesta == "s" or respuesta == "si" or respuesta == "S" or respuesta == "SI") :
     iniciar = True
   else:
     iniciar = False
     print("Gracias por utilizar los servicios")




