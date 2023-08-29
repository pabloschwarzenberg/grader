import re

class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.clave = ""
    
    def cambiar_password(self, password):
        if len(password) < 8 or len(password) > 16:
            return False
        
        # Verificar si la contraseña contiene letras y números
        if not re.search(r'[a-zA-Z]', password) or not re.search(r'\d', password):
            return False
        
        # Verificar si la contraseña contiene una letra mayúscula o un carácter especial
        if not re.search(r'[A-Z]', password) and not re.search(r'[^a-zA-Z0-9]', password):
            return False
        
        self.clave = password
        return True
    
    def login(self, password):
        return self.clave == password
