#Cajero Automático
cajero = 1000000

user = int(input("Ingrese su número de usuario: "))
passc = int(input("Ingrese su clave: "))

if user == 10310334151:
  usuario = 100000
  intentos = 0
  while True:
    if passc == 1803:
      ingreso = "N"
      while ingreso.isdgit() == True or ingreso == N:
        ingreso = input("Ingrese monto a extraer: ")
        if ingreso.isdigit():
          das = int(ingreso)
        else:
          continue
        if das > usuario:
          print("monto no permitido")
        else:
          cajero -= das
          usuario -= das
          print("saldo cuenta="+str(usuario))
          print("saldo cajero="+str(cajero))
    elif intentos == 3:
      print("tarjeta bloqueada")
      break
    else:
      intentos +=1
      print("clave invalida") 