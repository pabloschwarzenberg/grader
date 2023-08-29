class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        if 8<=len(password)<=16:
            a=0
            for i in password:
                if i.isupper()==True:
                    a+=1
                if i.isalnum()==False and i.isalpha()==False and i.isspace()==False:
                    a+=1
            if a!=0:
                Usuario.password=password
                return True
            else:
                return False
        else:
            return False
    def login(self,password):
        if password==Usuario.password:
            return True
        else:
            return False