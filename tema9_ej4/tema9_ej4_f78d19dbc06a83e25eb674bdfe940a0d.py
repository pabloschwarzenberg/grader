class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.password = ""

    def cambiar_password(self, password):
        if len(password) < 8 or len(password) > 16:
            return False
        if not any(char.isalpha() for char in password) or not any(char.isdigit() for char in password):
            return False
        if not any(char.isupper() for char in password) and not any(not char.isalnum() for char in password):
            return False

        self.password = password
        return True

    def login(self, password):
        return self.password == password


if __name__ == "__main__":
    usuario = Usuario("pablo", "phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))  # Output: False
    print(usuario.cambiar_password("clavesecreta1_"))  # Output: True
    print(usuario.cambiar_password("clavesecreta"))  # Output: False
    print(usuario.cambiar_password("clasesecreta1"))  # Output: False
    print(usuario.cambiar_password("claveSecreta1"))  # Output: True
    print(usuario.login("clavesecreta1_"))  # Output: True
    print(usuario.login("claveSecreta1"))  # Output: True