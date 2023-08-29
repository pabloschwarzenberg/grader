#Cajero Automático
from user import User
from card import Card
from admin import Admin
import random

class Atm:
    def __init__(self):
        self.user_dict = {}

    def welcome(self):
        print('*' * 30)
        print ('*' + "" * 6 + 'Abrir una cuenta (1)' + '' + 'Consulta (2)' + '' * 6 + '*')
                 print ("*" + "" * 6 + 'Retirada (3)' + + '' + 'Depósito (4)' + '' * 6 + '*')
                 print ("*" + "" * 6 + 'Transferir (5)' + '' + 'Cambiar contraseña (6)' + '' * 6 + '*')
                 print ("*" + "" * 6 + 'Bloquear (7)' + '' + 'Desbloquear (8)' + '' * 6 + '*')
                 print ("*" + "" * 6 + 'Cuenta de ventas (9)' + '' + 'Salir (0)' + '' * 6 + '*')
        print('*' * 30)
    def mkcard(self):
        cardid = ''
        for i in range(6):
            a = str(random.randint(0,9))
            cardid += a
        return cardid

if __name__ == '__main__':

    atm = Atm()
    admin = Admin('admin','123456')


    if admin.login():
        try:
            atm.user_dict = User.duqu()
        except Exception as e:
            print(' ')
        while True:
            atm.welcome()
            print(atm.user_dict)
                         choice = int (input ('Ingrese lo que quiere hacer:'))
            if choice == 1:
                                 nombre = entrada ('Ingrese nombre:')
                                 cid = input ('número de identificación:')
                                 tel = input ('Número de móvil:')
                                 pwd1 = input ('Ingresar contraseña:')
                                 pwd2 = input ('Reconfirmar contraseña:')
                if pwd1 == pwd2 :
                    num = atm.mkcard()
                                         money = int (input ('Ingrese el monto de apertura de la cuenta (> = 10 $):'))
                    if money < 10 :
                                                 print ('Cantidad muy pequeña, error al abrir la cuenta')
                        continue
                    card = Card(num,money,pwd2)
                    user = User(name,cid,tel,card)
                    atm.user_dict[num] = user
                    # User.xieru(fdy.user_dict)
                                         print ('La cuenta se abrió con éxito, su número de tarjeta es:% s saldo de la tarjeta% .2f:'% (num, dinero))
                else:
                                         print ('La contraseña no coincide, la apertura de la cuenta falló')


            elif choice == 2:
                                 num = input ('Ingrese el número de tarjeta:')
                if num in atm.user_dict:
                    user = atm.user_dict.get(num)
                    if user.card.clock == False:
                        for i in range(3):
                                                         pwd = input ('Ingrese la contraseña:')
                            if pwd == user.card.pwd:
                                                                 print ('Número de tarjeta:% s Nombre:% s Número de móvil:% s Saldo:% .2f ¥'%
                                      (num,user.name,user.tel,user.card.money))
                                break
                            else:
                                                                 print ('¡Contraseña incorrecta!')
                        else:
                                                         print ('¡Contraseña incorrecta tres veces, la tarjeta está bloqueada!')
                            user.card.clock = True

                                                         # '' 'Recuerde guardar la información del diccionario aquí nuevamente' ''
                            # User.xieru(fdy.user_dict)
                    else:
                                                 print ('¡Esta tarjeta está bloqueada, desbloquéala primero!')
                else:
                                         print ('¡El número de tarjeta no existe!')
            elif choice == 3:
                                 num = input ('Ingrese el número de tarjeta:')
                if num in atm.user_dict:
                    user = atm.user_dict.get(num)
                    if user.card.clock == False:
                        for i in range(3):
                                                         pwd = input ('Ingrese la contraseña:')
                            if pwd == user.card.pwd:
                                                                 qumoney = int (input ('Ingrese el monto del retiro:'))
                                if qumoney <= user.card.money:
                                    user.card.money-=qumoney
                                    # User.xieru(fdy.user_dict)
                                                                         print ('¡Retiro exitoso! Saldo de la tarjeta:% .2f ¥'% (user.card.money))
                                    break
                                else:
                                                                         print ('¡Fuera de balance!')
                                    break
                            else:
                                                                 print ('¡Contraseña incorrecta!')
                        else:
                                                         print ('¡Contraseña incorrecta tres veces, la tarjeta está bloqueada!')
                            user.card.clock = True
                            # User.xieru(fdy.user_dict)
                    else:
                                                 print ('¡Esta tarjeta está bloqueada, desbloquéala primero!')
                else:
                                         print ('¡El número de tarjeta no existe!')
            elif choice == 4:
                                 num = input ('Ingrese el número de tarjeta:')
                if num in atm.user_dict:
                    user = atm.user_dict.get(num)
                    if user.card.clock == False:
                        for i in range(3):
                                                         pwd = input ('Ingrese la contraseña:')
                            if pwd == user.card.pwd:
                                                                 qumoney = float (input ('Ingrese el monto del depósito:'))
                                user.card.money += qumoney
                                # User.xieru(fdy.user_dict)
                                                                 print ('¡Depósito exitoso! Saldo en la tarjeta:% .2f ¥'% (user.card.money))
                                break
                            else:
                                                                 print ('¡Contraseña incorrecta!')
                        else:
                            print ('¡Contraseña incorrecta tres veces, la tarjeta está bloqueada!')
                            user.card.clock = True
                            # User.xieru(fdy.user_dict)
                    else:
                                                 print ('¡Esta tarjeta está bloqueada, desbloquéala primero!')
                else:
                                         print ('¡El número de tarjeta no existe!')
            elif choice == 5:
                                 num = input ('Ingrese el número de tarjeta:')
                if num in atm.user_dict:
                    user = atm.user_dict.get(num)
                    if user.card.clock == False:
                        for i in range(3):
                                                         pwd = input ('Ingrese la contraseña:')
                            if pwd == user.card.pwd:
                                                                 qumoney = float (input ('Ingrese el monto de la transferencia:'))
                                                                 num1 = input ('Ingrese el número de tarjeta de la otra parte:')
                                if num1 in atm.user_dict:
                                    user1 = atm.user_dict.get(num1)
                                    if qumoney <= user.card.money:
                                                                                 print ('y: confirmar transferencia n: cancelar transferencia')
                                        answer = input('')
                                        if answer == 'y':
                                            user.card.money-=qumoney
                                            user1.card.money+=qumoney
                                            # User.xieru(fdy.user_dict)
                                                                                         print ('¡Transferencia exitosa! Saldo en la tarjeta:% .2f ¥'% (user.card.money))
                                            break
                                        elif answer == 'n':
                                                                                         print ('Transferido!')
                                            break
                                    else:
                                                                                 print ('Cantidad insuficiente')
                                        break
                                else:
                                                                         print ('¡El otro número de tarjeta no existe!')
                                    break
                            else:
                                                                 print ('¡Contraseña incorrecta!')
                        else:
                                                         print ('¡Contraseña incorrecta tres veces, la tarjeta está bloqueada!')
                            user.card.clock = True
                            # User.xieru(fdy.user_dict)
                    else:
                                                 print ('¡Esta tarjeta está bloqueada, desbloquéala primero!')
                else:
                                         print ('¡El número de tarjeta no existe!')
            elif choice == 6:
                                 num = input ('Ingrese el número de tarjeta:')
                if num in atm.user_dict:
                    user = atm.user_dict.get(num)
                    if user.card.clock == False:
                        for i in range(3):
                                                         pwd = input ('Ingrese la contraseña:')
                            if pwd == user.card.pwd:
                                                                 pwd1 = input ('Ingrese una nueva contraseña:')
                                                                 pwd2 = input ('Ingrese nuevamente una nueva contraseña:')
                                if pwd1 == pwd2 :
                                    user.card.pwd = pwd2
                                    # User.xieru(fdy.user_dict)
                                                                         print ('¡La contraseña cambió con éxito!')
                                    break
                            else:
                                                                 print ('¡Contraseña incorrecta!')

                        else:
                                                         print ('¡Contraseña incorrecta tres veces, la tarjeta está bloqueada!')
                            user.card.clock = True
                            # User.xieru(fdy.user_dict)
                    else:
                                                 print ('¡Esta tarjeta está bloqueada, desbloquéala primero!')
                else:
                                         print ('¡El número de tarjeta no existe!')
            elif choice == 7:
                                 num = input ('Ingrese el número de tarjeta:')
                if num in atm.user_dict:
                    user = atm.user_dict.get(num)
                                         pwd = input ('Ingrese la contraseña:')
                    if pwd == user.card.pwd:
                        user.card.clock = True
                        # User.xieru(fdy.user_dict)
                                                 print ('¡La tarjeta está bloqueada!')
                    else:
                                                 print ('¡Contraseña incorrecta!')
                else:
                                         print ('¡El número de tarjeta no es válido!')
            elif choice == 8:
                                 num = input ('Ingrese el número de tarjeta:')
                if num in atm.user_dict:
                    user = atm.user_dict.get(num)
                                         pwd = input ('Ingrese la contraseña:')
                    if pwd == user.card.pwd:
                        user.card.clock = False
                        # User.xieru(fdy.user_dict)
                                                 print ('¡Tarjeta desbloqueada!')
                    else:
                                                 print ('¡Contraseña incorrecta!')
                else:
                                         print ('¡El número de tarjeta no es válido!')
            elif choice == 9:
                                 num = input ('Ingrese el número de tarjeta:')
                if num in atm.user_dict:
                    user = atm.user_dict.get(num)
                    if user.card.clock == False:
                        for i in range(3):
                                                         pwd = input ('Ingrese la contraseña:')
                            if pwd == user.card.pwd:
                                                                 print ('¿Estás seguro de que deseas cancelar la cuenta?')
                                answer = input('y/n:')
                                if answer == 'y':
                                    atm.user_dict.pop(num)
                                                                         print ('¡Cancelación exitosa!')
                                    User.xieru(atm.user_dict)
                                    break
                                else:
                                                                         print ('¡Operación cancelada!')
                                    break
                            else:
                                print ('¡Contraseña incorrecta!')
                        else:
                                                         print ('¡Contraseña incorrecta tres veces, la tarjeta está bloqueada!')
                            user.card.clock = True
                            # User.xieru(fdy.user_dict)
                    else:
                                                 print ('¡Esta tarjeta está bloqueada, desbloquéala primero!')
                else:
                                         print ('¡El número de tarjeta no existe!')
            elif choice == 0:
            	             # El programa sale normalmente para guardar los datos (no se puede guardar si sale anormalmente)
                User.xieru(atm.user_dict)
                break

      