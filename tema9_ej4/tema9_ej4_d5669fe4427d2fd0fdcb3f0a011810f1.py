class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.clave = ""

    def cambiar_password(self, password):
        if 8 <= len(password) <= 16:
            has_uppercase = any(char.isupper() for char in password)
            has_special_char = any(
                char for char in password if not char.isalnum() and char != "#"
            )
            if has_uppercase or has_special_char:
                self.clave = password
                return True
        return False

    def login(self, password):
        return self.clave == password
