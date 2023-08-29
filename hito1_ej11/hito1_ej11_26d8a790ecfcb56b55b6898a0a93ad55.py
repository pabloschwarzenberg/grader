usuarioEnBD = "10334151"
claveEnBD = "1803"
sesion = False
saldo = 100000
saldo_cajero = 1000000
iniciar = True
contador = 1
conectado = bool
billete20 = 20000
billete10 = 10000
billete05 = 5000
billetes20000 = 20
billetes10000 = 40
billetes5000 = 40
caja = []


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
       b1 = 0
       b2 = 0
       b3 = 0
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
       billetes20000 = 20
       billetes10000 = 40
       billetes5000 = 40
       billete20 = 20000
       billete10 = 10000
       billete05 = 5000
       rt = valor
       b1 = int(valor / 20000);

       if (valor - (b1 * billete20 )) >= 0:
         valor = valor - (b1 * billete20);
         b2 = int(valor / 10000)
         print(b1)

         if (valor - (b2 * billete10)) >= 0:
           valor = valor - (b2 * billete10)
           b3 = int(valor / 5000)
           print(b2)

           if (valor- (b3 * billete05)) >= 0:
             valor = valor - (b3 * billete05)
             print(b3)

             ol0 = "billetes 20000=" + str(b1)               
             ol1 = "billetes 10000=" +str(b2)
             ol2 = "billetes 5000=" +str(b3)
             print(xd)
             print(xd2)
             print(ol0)
             print(ol1)
             print(ol2)


       
       
       
  



while (iniciar == True) :
  ejecutar()
  respuesta = input("¿Deseas realizar otra operación? presione N, cualquier otra cosa para salir ")
  if (respuesta == "N"):
    iniciar = True
  else:
    iniciar = False
    print("Adios...")
