#Cajero Automático
a=int(input("Ingrese usuario: "))
b=int(input("Ingrese clave: "))
c=int(input("Ingrese monto: "))
 
if a==10334151 and b==1803:
    print(str(c))
    if c<=100000:
       print("saldo cuenta="+str(100000-c))
       print("saldo cajero="+str(1000000-c))
    else:
       print("monto no permitido")

elif a==10334151 and b!=1803:
       print("clave invalida")
  

     