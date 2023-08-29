a=int(input("ingrese número de usuario: "))
k=3
if a==10334151:
    while k>0:
       b=input("ingrese clave: ")
       if b=="1803":
           d=100000
           e=1000000
           c=int(input("monto a retirar: "))
           if c>100000:
                print("monto no permitido")
           else:
                d= d-c
                e= e-c
                print("saldo cuenta= ",d)
                print("saldo cajero= ",e)
                x=input("¿Desea salir?")
                if x!="n":
                  break       
       else:
           print("clave inválida")
           k=k-1
           
           if k==0:
               print("tarjeta bloqueada")
               break
else:
  print("ingrese un usuario válido")
 
