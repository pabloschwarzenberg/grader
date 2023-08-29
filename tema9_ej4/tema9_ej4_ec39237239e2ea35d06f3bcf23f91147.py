class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.password = ""

    def cambiar_password(self, password):
        if self.validar_password(password):
            self.password = password
            return True
        else:
            return False

    def login(self, password):
        if self.password == password:
            return True
        else:
            return False

    def validar_password(self, password):
        if len(password) >= 8 and len(password) <= 16:
            has_letter = False
            has_digit = False
            has_uppercase = False
            has_special = False

            for char in password:
                if char.isalpha() and char.isupper():
                    has_uppercase = True
                elif char.isalpha():
                    has_letter = True
                elif char.isdigit():
                    has_digit = True
                else:
                    has_special = True

            if (has_letter or has_special) and has_digit and (has_uppercase or has_special):
                return True

        return False