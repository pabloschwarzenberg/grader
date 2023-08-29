#Cajero Automático
user = 10334151
pw = 1803 

user_money = 100000
cajero_money = 1000000

cont= 0

ingreso_user = int(input("Ingrese el usuario: "))
ingreso_pw = int(input("Ingrese su clave: "))
if ingreso_user != user or ingreso_pw != pw:
  cont = cont+1
  print("Datos ingresados no validos")
  ingreso_user1 = int(input("Ingrese el usuario: "))
  ingreso_pw1 = int(input("Ingrese su clave: "))
  if ingreso_user1 != user or ingreso_pw1 != pw:
    cont = cont + 1
    print("Datos ingresados no validos")
    ingreso_user2 = int(input("Ingrese el usuario: "))
    ingreso_pw2 = int(input("Ingrese su clave: "))
    if ingreso_user2 != user or ingreso_pw2 != pw:
        print("Cuenta Bloqueada")

if (ingreso_user == user and ingreso_pw == pw) or (ingreso_user1 == user and ingreso_pw1 == pw) or (ingreso_user2 == user and ingreso_pw2 == pw):
  retiro = int(input("Cuanto desea retirar?: "))
  new_user_money = user_money - retiro
  new_cajero_money = cajero_money - retiro
  print("saldo cuenta=", new_user_money)
  print("saldo cajero=", new_cajero_money)
      