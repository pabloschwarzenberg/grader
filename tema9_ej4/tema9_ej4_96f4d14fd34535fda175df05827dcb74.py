import re

class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.clave = ''  # La clave se inicializa como una cadena vacía
    
    def cambiar_password(self, password):
        if self.validar_password(password):  # Verificar si la contraseña cumple las reglas
            self.clave = password  # Actualizar la clave del usuario
            return True
        else:
            return False
    
    def validar_password(self, password):
        # Verificar la longitud de la contraseña
        if 8 <= len(password) <= 16:
            # Verificar si la contraseña contiene letras y números
            if re.search(r'[a-zA-Z0-9]', password):
                # Verificar si la contraseña contiene al menos una letra mayúscula o un carácter especial
                if re.search(r'[A-Z!@#$%^&*()_+]', password):
                    return True  # La contraseña cumple todas las reglas
        return False  # La contraseña no cumple alguna de las reglas
    
    def login(self, password):
        return self.clave == password  # Verificar si la contraseña ingresada coincide con la clave del usuario


