#Cajero Automático
try:
  contador = 1
  cajero = 1000000
  disponible = 100000
  usuario = str(input("Ingrese Usuario: "))
  while usuario != "10334151":
    usuario = str(input("Error, Ingrese Usuario: "))
  clave = str(input("Ingrese Clave: "))
  while clave != "1803":
    usuario = str(input("Error, Ingrese Clave: "))
    contador = contador + 1
    if contador == 3:
        print("Clave Bloqueada")
        break
  retiro = int(input("Que monto desea retirar: "))
  while retiro < 1 or retiro > disponible:
      retiro = int(input("Error, Que monto desea retirar: "))
  disponible = disponible - retiro
  cajero = cajero - retiro
  print("saldo cuenta=", disponible)
  print("saldo cajero=", cajero)
except EOFError:
  print("error")