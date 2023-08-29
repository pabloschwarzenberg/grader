class Usuario:

    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.clave = ""

    def cambiar_password(self, password):
        if 8 <= len(password) <= 16 and any(letra.isalpha() for letra in password) and any(caracter.isdigit() for caracter in password):
            if any(letra.isupper() for letra in password) or any(caracter.isalnum() == False and caracter.isalpha() == False for caracter in password):
                
                self.clave = password
                return True
        
        return False

    def login(self, password):
        if password == self.clave:
            return True
        return False