 [19:12, 4/7/2020] Isi Unab: def Monto(monto,Cajero=1000000,usuario=100000):
     if monto > Cajero:
         return "Monto no permitido"
     else:
         usuario = usuario-monto
         Cajero = Cajero-monto
         print("saldo cuenta=",usuario)
         print("saldo cajero=",Cajero)
         return [usuario,Cajero]

 c = 0
 b = 0
 intentos = 0
 while b == 0:
     if c == 0:
         print("Usuario")
         input()
         print("clave")
         clave = input()
         if clave == "1803":
             c = 1
         elif intentos == 2:
             print("Tarjeta bloqueada")
             break
         else:
             intentos += 1
     elif c == 1:
         print("Ingrese monto a retirar")
         p = input()
         di = "qwertyuiopñlkjhgfdsazxcvbm,.-{}+´¿QWERTYUIOPÑLKJHGFDSAZXCVBM"
         if p in di:
             break
         elif p == "N":
             c = 1
         else:
             Monto(float(p))
 [19:12, 4/7/2020] Isi Unab: from random import randint
 
 NumeroParaAdivinar = randint (1, 20)

 intentos = 0
 NumeroAdivinado = 0 

 while intentos <= 5:
       if intentos > 1:
             NumeroAdivinado = int(input("intenta de nuevo: "))
       else:
             NumeroAdivinado = int(input("digita el numero que crees que tengo: "))
       intentos += 1
       if NumeroAdivinado == NumeroParaAdivinar:
             print("Adivinaste, mi número era", NumeroParaAdivinar )
             break
       if  NumeroParaAdivinar > NumeroAdivinado:
           print ("Mi número es mayor ")
    
       else:
             print("Mi número es menor ")

       if intentos == 5:
             print("No adivinaste, mi número era", NumeroParaAdivinar )
             break