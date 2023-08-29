class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.clave = ""

    def cambiar_password(self, password):
        if len(password) < 8 or len(password) > 16:
            return False

        has_letter = False
        has_digit = False
        has_special_char = False

        for char in password:
            if char.isalpha():
                has_letter = True
            elif char.isdigit():
                has_digit = True
            else:
                has_special_char = True

        if has_letter and (has_digit or has_special_char):
            self.clave = password
            return True
        else:
            return False

    def login(self, password):
        return self.clave == password