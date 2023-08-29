class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.clave = ""

    def cambiar_password(self, password):
        if len(password) < 8 or len(password) > 16:
            return False

        has_uppercase = False
        has_special = False

        for char in password:
            if char.isupper():
                has_uppercase = True
            elif not char.isalnum():
                has_special = True

        if has_uppercase or has_special:
            self.clave = password
            return True
        else:
            return False

    def login(self, password):
        return self.clave == password