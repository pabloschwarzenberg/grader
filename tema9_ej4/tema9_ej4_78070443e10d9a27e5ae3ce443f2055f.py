class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.clave = ""

    def cambiar_password(self, password):
        if self.validar_password(password):
            self.clave = password
            return True
        else:
            return False

    def validar_password(self, password):
        if len(password) < 8 or len(password) > 16:
            return False

        has_uppercase = False
        has_special_char = False

        for char in password:
            if char.isalpha() and char.isupper():
                has_uppercase = True
            elif not char.isalnum():
                has_special_char = True

        return has_uppercase or has_special_char

    def login(self, password):
        return self.clave == password
