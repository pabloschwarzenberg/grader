#Cajero Automático
cajero=1000000
saldo=100000
end=0
x=0
while(end==0):
 user=int(input("INGRESE USUARIO :"))
 pw=int(input("INGRESE CONTRASEÑA :"))
 while(x<3):
   if(user==10334151 and pw==1803):
     while(end==0):
       print("Tu saldo actual es $",saldo)
       retiro=int(input("Monto a retirar :$"))
       if(retiro<saldo and retiro<cajero):
         saldo=saldo-retiro
         cajero=cajero-retiro
         print("saldo cuenta=",saldo)
         print("saldo cajero=",cajero)
         end=end+1
       else:
          print("mondo no permitido")
   else:
     print("clave invalida")
     x=x+1
 if(x==3):
   print("tarjeta bloqueada")
   end=end+1
 end=end+1