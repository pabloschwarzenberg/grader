class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.clave = ""

    def cambiar_password(self, password):
        if len(password) < 8 or len(password) > 16:
            return False

        has_letter = False
        has_number = False
        has_uppercase = False
        has_special_char = False

        for char in password:
            if char.isalpha() and not has_letter:
                has_letter = True
            elif char.isdigit() and not has_number:
                has_number = True
            elif char.isupper() and not has_uppercase:
                has_uppercase = True
            elif not char.isalnum() and not has_special_char:
                has_special_char = True

        if has_letter and has_number and (has_uppercase or has_special_char):
            self.clave = password
            return True
        else:
            return False

    def login(self, password):
        return self.clave == password
