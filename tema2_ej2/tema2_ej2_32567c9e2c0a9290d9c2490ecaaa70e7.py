def amigos(a,b): 
  div_de_numero=1 
  div_de_numero_1=1 
  suma_div_numero=0 
  suma_div_numero_1=0 
  while div_de_numero<a: 
    if a%div_de_numero==0: 
      suma_div_numero+=div_de_numero 
      print("divisor de %d es: %d" % (a,div_de_numero),"la suma de divisores de %d es: %d" %(a,suma_div_numero)) 
    div_de_numero+=1 
  while div_de_numero_1<b: 
    if b%div_de_numero_1==0: 
      suma_div_numero_1+=div_de_numero_1
      print("divisor de %d es: %d" % (b,div_de_numero_1),"la suma de divisores de %d es: %d" %(b,suma_div_numero_1)) 
    div_de_numero_1 += 1 
  if suma_div_numero==b and suma_div_numero_1==a: 
    return True 
  else: 
    return False 
try: 
 numero = int(input("Número 1: ")) 
 numero_1 = int(input("Número 2: ")) 
 print(amigos(numero,numero_1)) 
except: 
 print("Ingrese un Número")
[15:13]
CAJERO AUTOMATICO NVL 1
[15:13]
# Saldo cajero
saldo_cajero = 1000000
# nombre Real tratado como numero, o sea, int()
usuario_verdadero = 10334151
# clave Real tratar como numero int()
clave_real = 1803
# saldo inicial usuario $100.000
saldo_inicial = 100000

# pedir usuario
print("Ingrese nombre de usuario: ")
usuario = int(input())


# contador para intentos
intentos = 0
while intentos < 3:
    # tratar todos los input como numeros int()

    # pedir clave
    print("Ingrese clave: ")
    clave = int(input())

    # Validar clave y Monto a retirar
    if clave == clave_real:
        print("¿Cuanto dinero desea retirar?")
        monto = int(input())

        # Validar monto del cajero vs monto pedido
        if monto <= saldo_cajero and monto <= saldo_inicial:
        # Validar el monto pedido vs monto en mi cuenta

            # Operacion matematicas
            # Descontar plata del usuario
            saldo_restante_usuario = saldo_inicial - monto

            # Descontar dinero retirado a saldo del cajero
            saldo_cajero_final = saldo_cajero - monto

            print("Saldo Cuenta= ", saldo_restante_usuario )
            print("Saldo Cajero= ", saldo_cajero_final)
            break
        else:
            print("Monto no permitido")
            break

    else:
        print("Clave Incorrecta, intente nuevamente")
        intentos = intentos + 1  #  otroa forma de escribir -> intentos += 1

if intentos == 3:
    print("Tarjeta Bloqueada")

print("Muchas gracias!!")
[15:14]
JUEGO ADIVINA MI NUMERO
[15:14]
import random
i=0
numero=random.randint(0, 20)
print ("hola amig@,adivina cual es el numero que estoy pensando,el numero esta entre 0 y 20.")

while (i)<5:
    print ("ingresa el numero que crees que es:")
    n_usuario= int(input())

    if n_usuario == numero:
        print("usted a adivinado")
        break

    elif (n_usuario) <(numero):
        i=+1
        print ("el numero muy bajo")
    elif (n_usuario) > (numero):
        i=+1
        print ("el numero es muy alto")
    else:
        break

print("El programa ha terminado")
[15:14]
FACTORES PRIMOS
[15:14]
def es_primo(numero):

  if numero >1:

    a=0

    divisor=2

    while divisor<numero:

      resto = numero%divisor

      if resto==0:

        a+=1

      divisor+=1

    if a==0:

      return True

    else:

      return False

  else:

    return False



try:

  numero_ingreso = int(input("Ingrese número: "))

  print(es_primo(numero_ingreso))

except:

  print("Ingrese sólo número por favor")