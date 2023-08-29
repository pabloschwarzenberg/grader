#Cajero Automático
user = int(input("User:"))


saldocajero = 1000000
cuenta = 100000
salir = ""
con = 0

if user == 10334151:
   while con != 3 and salir != "N":
    clave = int(input("Clave: "))
    if clave == 1803:
       while salir != "N":
          montret = int(input('Monto a retirar: '))
          if montret<= cuenta:
            cuenta = cuenta -montret
            saldocajero=saldocajero-montret
            print('saldo cuenta='+str(cuenta))
            print('saldo cajero='+str(saldocajero))
          else:
            print('monto no permitido')
          salir = (input('S/N')).upper()
        
    else:
      con +=1
      print('clave invalida')
    
   if con == 3:
     print("tarjeta bloqueada")   