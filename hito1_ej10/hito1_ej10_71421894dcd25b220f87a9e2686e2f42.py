#Cajero Automático
print("Welcome to Banco de xoro Chileno, solo cuenta corriente")
inicio=("N")
restar=("n","NO","no",)
chances = 0
Dinerototaldecajero= 1000000
Dinero= 100000
retirar_dinero=0
while inicio == "N":
 user = int(input("ingrese nombre de usario: "))
 if(user == 103):
     if(chances >= 3):
         print("valiste wey")
     else:
         print("Bienvenido a ver su dinerito")
     while chances < 3:
      password = int(input("Ingrese su contrasena: "))
      if password== 18:
        print("clave correcta")
        print("Cuenta Corriente,tu dinero es  "+str(Dinero))
        retirar_dinero= 1
        break
      elif chances <= 2:
        print("clave invalida")
        chances +=1
      if chances == 3:
        print("valiste wey")
 else:
    print("Usario incorrecto")
 if retirar_dinero  == 1:
        break
while retirar_dinero == 1:
    volver_a_intentar= 0
    dinero_a_retirar= int(input("Cuanto desea girar: $"))
    if (dinero_a_retirar > Dinero) or (dinero_a_retirar > Dinerototaldecajero):
        print("Monto no permitido")
        volver_a_intentar = 1
    else:
        print("Dinero retirado $"+str(dinero_a_retirar))
        Dinero= Dinero- dinero_a_retirar
        Dinerototaldecajero= Dinerototaldecajero - Dinero
        print("Saldo cuenta="+str(Dinero))
    if volver_a_intentar != 1:
       retirar= str(input("Para salir ingrese una letra distinta de N: "))
       if(retirar !="N") or (Dinerototaldecajero == 0):
        print("Hasta pronto!")
        incio = "S"
        break