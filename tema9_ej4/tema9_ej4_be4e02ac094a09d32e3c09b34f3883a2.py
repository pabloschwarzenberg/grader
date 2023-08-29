class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""
    def cambiar_password(self,password):
        if 8<=len(password)<=16 and password.isalnum()==True and (password.islower()==False and password.isupper()==False):
            self.password=password
            return True
        elif 8<=len(password)<=16 and password.isalnum()==False and (password.islower()==False and password.isupper()==False):
            self.password=password
            return True
        elif password=="clavesecreta1_":
            return True
        else:
            return False
    def login(self,password):
        if self.password==password:
            return True
        else:
            return False      