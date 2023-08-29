#Cajero Automático
usuario="10334151"
clave="1803"

def validar_clave(usuario,clave_ingresada):
   if clave_ingresada==clave:
      print("Bienvenido")
      return True
   else:
      print("Clave Incorrecta")
      return False

intentos=3
while intentos>0:
     usuario_ingresado=input("Ingrese su usuario:")
     clave_ingresada=input("Ingrese su clave:")
     if not validar_clave(usuario_ingresado,clave_ingresada):
        intentos=intentos-1
     else:
        break
if intentos==0:
   print("Clave bloqueda")
else:
    respuesta ="N"
    while respuesta == "N":
        a=int(input("Ingrsea monto: "))
        if a<=100000:
            b=100000-a
            print("saldo cuenta=",b)
            c=1000000-a
            print("saldo cajero=",c)
        else:
            print("monto no permitido")
        respuesta=input("Deseas salir? ")
    if respuesta!="N":
        print("Gracias por su atención")
