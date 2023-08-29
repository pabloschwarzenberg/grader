saldocajero=1000000

saldoinicial=100000

bill20000=20

bill10000=40

bill5000=40

usuario=int(input("ingrese su usuario:"))

while usuario !=10334151: #validar usuario

   usuario = int(input("error, ingrese usuario:"))

           

claveusuario=int(input("ingrese su clave:"))

contador=0

while not(claveusuario==1803):#clave!1803

   contador= contador+1

   if contador==3:

    print("tarjeta bloqueada")

    break

   else:

    claveusuario=int(input("ingrese su clave:"))

if contador !=3:#(esta se ejecuta cuando la clave es correcta y intentos <=3) o cuando los intentos =3

 



 montoaretirar=int(input("ingrese su monto:"))

 if montoaretirar<=saldocajero:

   if montoaretirar<=saldoinicial:

     saldocajero=saldocajero-montoaretirar

     saldoinicial=saldoinicial-montoaretirar

     retira20mil=0

     retira10mil=0

     retira5mil=0

     while ():

       if montoaretirar >=20000 and bill20000>0 :

         retira20mil=retira20mil+1

         bill20000=bill20000-1

         montoaretirar=montoaretirar-20000

       

       if montoaretirar>=5000 and bill5000>0:

         retira5mil=retira5mil+1

         bill5000=bill5000-1

         montoaretirar=montoaretirar-5000

         

    

 print("saldo cuenta=",saldoinicial)

 print("saldo cajero=",saldocajero)

 print("billetes 20000=",retira20mil)

 print("billetes10000=",retira10miL)

 print("billetes5000=",retira5mil)

   else:    

     print("monto invalido")

else:    

   print("monto invalido")

    