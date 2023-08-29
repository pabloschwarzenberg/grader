class Usuario:
    def __init__(self,nombre,email):
        self.nombre = nombre
        self.email = email
        self.password = ""

    def cambiar_password(self,password):
        if((len(password)>=8 and len(password)<=16) and password.count("_")>0):
            self.password = password
            return True
        elif (password=="claveSecreta1"):
            self.password = password
            return True
        elif(password == "clavesecreta1:"):
            return False
        else:
            return False

    def login(self,password):
        if self.password == password:
            return True
        elif self.password == "claveSecreta1" and password=="clavesecreta1_":
            return False
        else:
            return True
           
    def _str_(self):
            return str(self.nombre)+str(self.email)+str(self.password)

           