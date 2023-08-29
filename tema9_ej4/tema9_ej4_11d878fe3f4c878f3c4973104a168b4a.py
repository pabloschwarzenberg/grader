import re;

class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        resultado = False
        if len(password) >= 8 and len(password) <= 16:
            mayusculas = re.search("[A-Z]", password)
            guion = re.findall("_", password)
            signos = re.findall("\W", password)
            if mayusculas or len(signos) > 0 or len(guion) > 0:
                resultado = True
        else:
            resultado = False

        return resultado

    def login(self,password):
        if self.password == password:
            return True
        else:
            return False