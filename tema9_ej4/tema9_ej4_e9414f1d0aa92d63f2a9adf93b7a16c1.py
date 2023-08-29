class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.clave = ''

    def cambiar_password(self, password):
        if len(password) >= 8 and len(password) <= 16:
            has_uppercase_or_special = any(c.isupper() or not c.isalnum() for c in password)
            has_lowercase_and_number = any(c.islower() and c.isdigit() for c in password)
            if has_uppercase_or_special or has_lowercase_and_number:
                self.clave = password
                return True
        return False

    def login(self, password):
        return self.clave == password
