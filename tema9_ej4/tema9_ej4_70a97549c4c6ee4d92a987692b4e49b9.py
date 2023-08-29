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
        has_special = False
        for char in password:
            if char.isalpha():
                has_letter = True
            elif char.isdigit():
                has_number = True
            elif not char.isalnum():
                has_special = True
        if has_letter and has_number and (has_special or any(char.isupper() for char in password)):
            self.clave = password
            return True
        else:
            return False

    def login(self, password):
        return self.clave == password

if __name__ == "__main__":
    usuario = Usuario("pablo", "phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))  # False
    print(usuario.cambiar_password("clavesecreta1_"))  # True
    print(usuario.cambiar_password("clavesecreta"))  # False
    print(usuario.cambiar_password("clasesecreta1"))  # False
    print(usuario.cambiar_password("claveSecreta1"))  # True
    print(usuario.login("clavesecreta1_"))  # False
    print(usuario.login("claveSecreta1"))  # True