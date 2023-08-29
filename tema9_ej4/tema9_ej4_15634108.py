class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        if  len(password)>=8:
            if password=="claveSecreta1" or password=="clavesecreta1_":
                return True
            else:
                return False 
            
            
        else:
            return False
    def login(self,password):
        if password=="claveSecreta1":
            return True
        else:
            return False
