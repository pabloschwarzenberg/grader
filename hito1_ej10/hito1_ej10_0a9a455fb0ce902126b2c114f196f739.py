#Cajero Automático

saldo_inicial = 1000000
saldo_usuario = 100000

clave = 1803
usuario = 10334151
oport = 0
ingrese_clave = 0

salir = ""
while salir != "N": 

  while ingrese_clave != clave and oport < 3:
    ingrese_clave = int(input("Ingrese su clave: "))
    if ingrese_clave != clave:
      print("Clave invalida")
    elif ingrese_clave == clave:
      print("Acceso concedido")
      monto = int(input("Cuanto desea retirar?: "))
      if monto > saldo_usuario:
        print("Monto no permitido")
      else: 
        print("Su saldo despues del retiro es: ", saldo_usuario - monto)
        print("Saldo cajero", saldo_inicial - monto)
    oport +=1
  if oport >=3:
    print("Tarjeta bloqueada")
  #salir = input("Desea salir?: ")
if salir == "N":
  print("Ha Finalizado su sesion")