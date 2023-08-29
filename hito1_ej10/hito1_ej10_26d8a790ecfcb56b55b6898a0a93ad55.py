usuarioEnBD = "10334151"
claveEnBD = "1803"
sesion = False
saldo = 100000
saldo_cajero = 1000000
iniciar = True
contador = 1
conectado = bool

def validarUsuario(usuario, clave) :
  global sesion
  global contador
  if usuario == usuarioEnBD and clave == claveEnBD:
    sesion = True
    return True  
  if claveEnBD != clave:
    while contador < 3:
      contador = contador + 1
      print("clave invalida")
      clave = input("Digite contraseña: ")
      if clave == claveEnBD:
        break
      if contador == 3:
        print("tarjeta bloqueada")
        sesion = False
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
       print("valor invalido")
       return False, saldo

     saldo = saldo - valor
     return True, saldo


def ejecutar() :
       global saldo
       if not login() :
         iniciar = False
         print("tarjeta invalida")

       valor = int(input("Ingrese monto a retirar: "))
       while valor > saldo or valor < 0:
         print("monto invalido")
         valor = int(input("Ingrese monto a retirar: "))
         

       saldo_cajero_cajero = saldo_cajero - valor
       saldo_cuenta =  saldo - valor
       xd = "saldo cuenta=" + str(saldo_cuenta)
       xd2 = "saldo cajero=" + str(saldo_cajero_cajero)
       print(xd)
       print(xd2)
  

  


while (iniciar == True) :
  ejecutar()
  respuesta = input("¿Deseas realizar otra operación? presione N, cualquier otra cosa para salir ")
  if (respuesta == "N"):
    iniciar = True
  else:
    iniciar = False
    print("Adios...")

