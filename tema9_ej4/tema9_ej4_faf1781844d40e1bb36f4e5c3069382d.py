class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.password = ""

    def cambiar_password(self, password):
        if len(password) >= 8 and len(password) <= 16:
            has_letter = False
            has_number = False
            has_special_char = False

            for char in password:
                if char.isalpha():
                    has_letter = True
                elif char.isdigit():
                    has_number = True
                else:
                    has_special_char = True

            if has_letter and has_number and (has_special_char or any(char.isupper() for char in password)):
                self.password = password
                return True

        return False

    def login(self, password):
        return password == self.password


if __name__ == "__main__":
    usuario = Usuario("pablo", "phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))
