#Cajero Automático
nombre_de_usuario = int(input("proceda a colocar su usuario: "))

contrasena_usuario_banco = int(input("proceda a colocar su clave: "))

numero_de_intentos = 1
cajero_total_saldos= 1000000
usuario_saldo_total = 100000
nombre_de_usuario = 10334151
contrasena_cajero = 1803

b_20_lucas = 20000
b_10_lucas = 10000
b_5_lucas = 5000  

def bills(c,x):
  total_billetes = c // x
  resto = c % x
  return total_billetes,resto


while contrasena_usuario_banco != contrasena_cajero:
  numero_de_intentos += 1
  if contrasena_usuario_banco == contrasena_cajero:
    print("clave incorrecta")
    break
    
  if numero_de_intentos > 3:
    break
  print("clave invalida")

  contrasena_usuario_banco = int(input("Ingrese de nuevo su clave: "))


if numero_de_intentos > 3:
  print("tarjeta bloqueada")

if nombre_de_usuario == nombre_de_usuario :
  if contrasena_usuario_banco == contrasena_cajero:

    monto = int(input("¿Cuanto quiere retirar?: "))
    if monto > cajero_total_saldos and monto > cajero_total_saldos:
      print("monto no perimitido")

    else:
    
      usuario_saldo_total -= monto
      cajero_total_saldos -= monto
      b, r = bills(monto, b_20_lucas)
      c , r = bills(r , b_10_lucas)
      j , r = bills(r, b_5_lucas)

      print("saldo cuenta="+str(usuario_saldo_total))
      print("saldo cajero="+str(cajero_total_saldos))
      print("billetes20000="+str(b))
      print("billetes10000="+str(c))
      print("billetes5000="+str(j)) 