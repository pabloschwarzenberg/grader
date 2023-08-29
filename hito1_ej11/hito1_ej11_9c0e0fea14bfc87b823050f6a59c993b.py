# Ingresamos el numero y la clave para el usuario
usuario1 = 10334151
clave1 = 1803

#saldo que tiene la persona
saldo = 100000
#saldo del cajero automatico
saldo_auto = 1000000



#VERIFICADOR DE USUARIO Y CONTRASEÑA 
contador = 1
while contador <= 3:
    usuario = int(input("Ingresa el Usuario: "))
    clave = int(input("Ingresa la clave: "))

#SI EL USUARIO Y LA CONTRASEÑA FUERON UN EXITO
    if ((usuario == usuario1) and (clave == clave1)):
     contador = 4
    else:

     print("clave invalida")
    if (contador == 3):
        
        print("tarjeta bloqueada")
        break
    contador = contador +1

else:

          print("100.000")
          dinero_retiro = int(input("Cuanto dinero deseas retirar: "))

          if((dinero_retiro > 100000) or (dinero_retiro < 0)):
           print("monto no permitido")

          else:
              if((dinero_retiro <= 100000) or (dinero_retiro == 0)):
               print()

resultado1= saldo - dinero_retiro
resultado2= saldo_auto - dinero_retiro

print("saldo cuenta=",resultado1, "," "saldo cajero=",resultado2)

billetes_5000 = 40
billetes_10000 = 40
billetes_20000 = 20

def sacar_billetes(cantidad):
    global billetes_20000, billetes_10000, billetes_5000
    if cantidad <= 20000 * billetes_20000 + 10000 * billetes_10000 + 50000 * billetes_5000:

        de20000 = int(cantidad / 20000)
        cantidad = cantidad % 20000
        if de20000 >= billetes_20000:
         cantidad = cantidad + (de20000 - billetes_20000) * 20000
         de20000 = billetes_20000

        de10000 = int(cantidad / 10000)
        cantidad = cantidad % 10000
        if de10000 >= billetes_10000:
         cantidad = cantidad + (de10000 - billetes_10000) * 10000
         de10000 = billetes_10000

        de5000 = int(cantidad / 5000)
        cantidad = cantidad % 5000
        if de5000 >= billetes_5000:
         cantidad = cantidad + (de5000 - billetes_5000) * 5000
         de5000 = billetes_5000

        if cantidad ==0:
                billetes_20000 == billetes_20000 - de20000
                billetes_10000 == billetes_10000 - de10000
                billetes_5000 == billetes_5000 - de5000
                return [de20000, de10000, de5000]

        else:
            return [0, 0, 0]

    else:
                return [-1, -1, -1]

try:

    resultado = sacar_billetes(dinero_retiro)
    if resultado == [0, 0, 0]:
        print ()
    elif resultado == [-1, -1, -1]:
        print ()

    else:

        print("billetes 20000="+str(resultado[0]))
        print("billetes 10000="+str(resultado[1]))
        print("billetes 5000="+str(resultado[2]))
except:
    print()

else:
           if(dinero_retiro > 100000):
            print()
           if(dinero_retiro < 0):
            print()


           else: 
             if((dinero_retiro <= 100000) or (dinero_retiro == 0)):
              print()
