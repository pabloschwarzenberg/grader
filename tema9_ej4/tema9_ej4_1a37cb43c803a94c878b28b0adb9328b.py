import re

class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.clave = ""

    def cambiar_password(self, password):
        """
        Actualiza la clave del usuario si la contraseña cumple las reglas
        """
        # Verificar longitud de la contraseña
        if len(password) < 8 or len(password) > 16:
            return False
        # Verificar que la contraseña contenga letras y números
        if not re.search("[a-zA-Z]", password) or not re.search("[0-9]", password):
            return False
        # Verificar que la contraseña contenga al menos una letra mayúscula o un carácter especial
        if not re.search("[A-Z!@#$%^&*()_+]", password):
            return False
        
        self.clave = password
        return True
    
    def login(self, password):
        """
        Retorna True si la contraseña ingresada corresponde a la clave del usuario
        """
        if self.clave == password:
            return True
        else:
            return False
