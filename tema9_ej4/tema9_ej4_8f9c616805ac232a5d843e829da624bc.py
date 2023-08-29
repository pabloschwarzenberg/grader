class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.clave = ""

    def cambiar_password(self, password):
        if 8 <= len(password) <= 16:
            has_uppercase = False
            has_special_char = False

            for char in password:
                if char.isupper():
                    has_uppercase = True
                elif not char.isalnum() and char != '#':
                    has_special_char = True

            if has_uppercase or has_special_char:
                self.clave = password
                return True

        return False

    def login(self, password):
        return self.clave == password
