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
        has_special_char = False

        for char in password:
            if char.isalpha() and char.isupper():
                has_letter = True
            elif char.isdigit():
                has_number = True
            elif not char.isalnum():
                has_special_char = True

        if has_letter and (has_number or has_special_char):
            self.clave = password
            return True

        return False

    def login(self, password):
        return self.clave == password


if __name__ == "__main__":
    usuario = Usuario("pablo", "phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clavesecreta1_"))
