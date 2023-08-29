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
                        f=int(C/20000)
                        g=int((C - f * 20000) / 10000)
                        h=int((C - f * 20000 - g * 10000) / 5000) 
            
                        print("saldo cuenta=", E-C)
                        print("saldo cajero=", D-C)
                        print("billetes 20000=", f)
                        print("billetes 10000=", g)
                        print("billetes 5000=", h)
                        print("Gracias por confiar en nosotros.")

      else:
            C=int(input("Ingrese monto a retirar:"))

            if C>100000:
                  print("Monto no permitido.")
                  sys.exit(2)

            else:
                   D=1000000
                   E=100000
                   f=int(C/20000)
                   g=int((C - f * 20000) / 10000)
                   h=int((C - f * 20000 - g * 10000) / 5000) 
            
                   print("saldo cuenta=", E-C)
                   print("saldo cajero=", D-C)
                   print("billetes 20000=", f)
                   print("billetes 10000=", g)
                   print("billetes 5000=", h)
                   print("Gracias por confiar en nosotros.")

else:
      C=int(input("Ingrese monto a retirar:"))
      if C>100000:
            print("Monto no permitido.")
            sys.exit(2)
      else:
            D=1000000
            E=100000
            f=int(C/20000)
            g=int((C - f * 20000) / 10000)
            h=int((C - f * 20000 - g * 10000) / 5000) 
            
            print("saldo cuenta=", E-C)
            print("saldo cajero=", D-C)
            print("billetes 20000=", f)
            print("billetes 10000=", g)
            print("billetes 5000=", h)
            print("Gracias por confiar en nosotros.")

