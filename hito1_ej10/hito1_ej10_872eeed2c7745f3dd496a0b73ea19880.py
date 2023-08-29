#Cajero Automático
import sys

u=input("Ingrese su número de usuario:")
u=int(u)

sca=1000000

sca=int(sca)

scu=100000

scu=int(scu)

i=1
i=int(i)

while (u==10334151 and i<=3):

    c=input("Ingrese su clave:")

    c=int(c)
    
    
    if c==1803:

        while 1==1:

            m=input("Digite monto:")

            m=int(m)

            if m<=scu:

                scu=(scu-m)

                sca=(sca-m)

                print("Saldo cuenta:",scu)

                print("Saldo cajero:", sca)

                n=input("Si quiere realizar otra operación pulse la letra N")

                if n=="N":
                    continue
                elif n!="N":

                    sys.exit(0)
                
            elif m>scu :
                
                print("Monto no permitido")

                continue

    elif c!=1803:

        print("Clave inválida")

        i=i+1

if i==4:
    print("Tarjeta bloqueada")

    sys.exit(0)
        
                 
      