#Cajero Automático
cajero = 1000000
saldo = 100000

while saldo > 0:
  
  usuario = int(input("Ingrese numero de usuario: "))

  if usuario == 10334751:
  
    clave = int(input("Ingrese su clave: "))
  
    if clave != 1803:
      print("Clave invalida")
      clave = int(input("Ingrese su clave: "))
    
      if clave != 1803:
         print("Clave invalida")
         clave = int(input("Ingrese su clave: "))
       
         if clave != 1803:
           print("Tarjeta Bloqueada")
           exit
    else:
      
    
      retiro = int(input("Monto a retirar: "))
      
      if retiro > saldo:
        print("Monto no permitido")
      else:
        c = cajero - retiro
        s = saldo - retiro
         
        
        cajero = c
        saldo = s
        
        print("Saldo cuenta: ", c)
        print("Saldo cajero: ", s)
        
        b = input("Para hacer otra operacion oprima N: ")
        
        if b != "N":
          exit
      
  else:
    print("Usuario incorrecto")