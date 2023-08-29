class Usuario:
    def __init__(self,nombre,email):
        self.nombre= nombre
        self.clave= ""
        self.email= email
    def cambiar_password(self,password):
        numeros="1234567890"
        letras="abcdefghijklmnopqrstuvwxyz"
        if 7<len(password)<17:
            for i in password:
                for n in numeros:
                    for l in letras:
                        if i == n o i== l:
                            self.clave = password
                            return True
                        else:
                            return False
    def login(self,password):
        if password == self.clave:
            return True
        else:
            return False