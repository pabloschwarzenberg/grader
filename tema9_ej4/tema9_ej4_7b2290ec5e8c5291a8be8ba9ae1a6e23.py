import re



class Usuario:

    nombre=''

    email=''



    def __init__(self,nombre,email):

        self.nombre=nombre

        self.email=email

        self.password=''



    def cambiar_password(self,password):

        if len(password)>=8 and len(password)<=16:

            if re.search('[a-z]', password) and re.search('[0-9]', password) and (re.search('[$@#_]', password) or re.search('[A-Z]' , password)):

                self.password=password

                return True

            else:

                return False    

        else:

            return False

    

    def login(self,password):

        if password==self.password:

            return True

        else:

            return False



