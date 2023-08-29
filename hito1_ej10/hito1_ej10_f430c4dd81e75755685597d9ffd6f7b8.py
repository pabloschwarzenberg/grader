import sys

n=int(input("Ingrese número de usuario:"))
B=int(input("Ingrese clave:"))

if n!=10334151:
      print("Usuario inválido")

if B!=1803:
      print("Clave invalida, ingrese nuevamente.")
      B=input("Ingrese clave:")

      if B!="1803":
            print("Clave invalida, ingrese nuevamente.")
            B=input("Ingrese clave:")

            if B!="1803":
                  print("Clave invalida, tarjeta bloqueada.")
                  sys.exit(2)

            else:
                  C=int(input("Ingrese monto a retirar:"))

                  if C>100000:
                        print("Monto no permitido.")
                        sys.exit(2)

                  else:
                        D=1000000
                        E=100000
                        print("saldo cuenta=", E-C)
                        print("saldo cajero=", D-C)
                        print("Gracias por confiar en nosotros.")

      else:
            C=int(input("Ingrese monto a retirar:"))

            if C>100000:
                  print("Monto no permitido.")
                  sys.exit(2)

            else:
                  D=1000000
                  E=100000
                  print("saldo cuenta=", E-C)
                  print("saldo cajero=", D-C)
                  print("Gracias por confiar en nosotros.")

else:
      C=int(input("Ingrese monto a retirar:"))
      if C>100000:
            print("Monto no permitido.")
            sys.exit(2)
      else:
            D=1000000
            E=100000
            print("saldo cuenta=", E-C)
            print("saldo cajero=", D-C)
            print("Gracias por confiar en nosotros.")
