class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.clave = ''

    def cambiar_password(self, password):
        if len(password) < 8 or len(password) > 16:
            return False

        has_uppercase = False
        has_special_char = False

        for char in password:
            if char.isalpha() and char.isupper():
                has_uppercase = True
            elif not char.isalnum():
                has_special_char = True

        if not has_uppercase and not has_special_char:
            return False

        self.clave = password
        return True

    def login(self, password):
        return self.clave == password

