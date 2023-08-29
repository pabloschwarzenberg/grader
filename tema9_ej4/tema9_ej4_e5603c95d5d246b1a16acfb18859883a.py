class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.clave = ''

    def cambiar_password(self, password):
        if self.validar_password(password):
            self.clave = password
            return True
        else:
            return False

    def validar_password(self, password):
        if len(password) < 8 or len(password) > 16:
            return False

        has_letter = False
        has_number = False
        has_uppercase = False
        has_special = False

        for char in password:
            if char.isalpha():
                has_letter = True
                if char.isupper():
                    has_uppercase = True
            elif char.isdigit():
                has_number = True
            else:
                has_special = True

        return has_letter and has_number and (has_uppercase or has_special)

    def login(self, password):
        return password == self.clave
           