#Cajero Automático
i = 0

while i<3:

      usuario=input("ingrese su nombre de usuario")

      i=i +1

      if str(usuario)=="10334151":

            print("USUARIO CORRECTO")

            clave=input("ingrese su clave")

            if str(clave)=="1803":

                  print("Bienvenido 10334151")
                  saldocajero = 1000000
                  saldoi = 100000
                  saldof = int(input("Ingrese el monto a retirar: "))

                  if saldof > saldof:
                    print("monto no permitido")
                    break

                  if saldof < saldoi:
                    saldofinal = saldoi - saldof
                    saldocajerof = saldocajero - saldof
                    print("saldo cuenta =",saldofinal)
                    print("saldo cajero =",saldocajerof)
                    break
                  
            else:

                  print("clave invalida")

                  if    i==3:

                        print("INTENTOS AGOTADOS")

                        break

      else:

            print("USUARIO INCORRECTO")

            if    i==3:

                  print("tarjeta bloqueada")
