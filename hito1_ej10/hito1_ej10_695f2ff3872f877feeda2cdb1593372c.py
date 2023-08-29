#Cajero Automático
#a=saldo cajero
a=1000000
print(a)
#b=saldo cuenta 
b=100000
print(b)
estaRegistrado=False

i=1
while i<4:
    if not estaRegistrado:
        print("ingresar usuario")
        #u=usuario cuenta
        u=int(input())
        print("ingresar clave")
        #c=clave cuenta
        c=int(input())
    if(u==10334151):
        if(c==1803):
            estaRegistrado=True
            print("monto a retirar")
            #m=monto a retirar
            m=(input())
            m=int(m)
            if m<=b:
                #d=saldo cuenta despues de retirar
                d=(b-m)    
                e=(a-m)
                print("saldo cuenta=",d)
                print("saldo cajero=",e)
                a=input()
                if a!="N":
                  print("salir")
                  break
            else:
              print("monto no permitido")
         
        else:
            print("clave invalida")
            i=i+1
if (i>3):
    print("tarjeta bloqueda")




