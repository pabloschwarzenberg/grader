#Cajero Automático

intentos = 0
user = input("Usuario: ")
#pw = input("Ingrese contraseña: ")

cajero = 1000000
cuenta = 100000

num = input("Ingrese contraseña: ")


def validar(n):
  if n == "1803":
    return True
  elif n == "N":
    return "N"
  else: return False
    
    
def resultado():
  print("saldo cuenta="+str(cuenta))
  print("saldo cajero="+str(cajero))

while True:
  aux = validar(num)
  if aux == "N":
    break
  elif aux == True:
      entrada = input("Ingrese monto a retirar: ")
      if entrada != "N":
        if (int(entrada) <= cuenta) and (int(entrada) <= cajero):
          cuenta -= int(entrada)
          cajero -= int(entrada)
          resultado()
        else:
          print("monto no permitido")
      else:
        break
  else:
      print("clave invalida")
      intentos+=1
      if intentos>=3:
        print("tarjeta bloqueada")
        break

if intentos<3:
	print(resultado())

