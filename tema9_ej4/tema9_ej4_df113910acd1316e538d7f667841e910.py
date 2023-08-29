from sys import flags


class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
  
        long_val = False
        tiene_letra = False
        tiene_mayuscula = False
        tiene_num = False
        tiene_car_esp = False


        if len(password) >= 8 and len(password)<= 16:
            for c in password:
                if c.isalpha():
                    tiene_letra = True

                if c.isdigit():
                    tiene_num = True

                if (65<=ord(c)<=90):
                    tiene_mayuscula = True

                if (32<=ord(c)<=47) or (58<=ord(c)<=64) or (91<=ord(c)<=96) or (123<=ord(c)<=1):
                    tiene_car_esp = True

            if tiene_letra and tiene_num and (tiene_mayuscula or tiene_car_esp):
                self.password = password
                return True
            else:
                return False
        else:
            return False

    def login(self,password):

        if password == self.password:
            return True
        else:
            return False 
