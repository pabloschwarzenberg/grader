class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.password = ""

    def cambiar_password(self, password):
        if (
            len(password) >= 8
            and len(password) <= 16
            and (any(char.isupper() for char in password) or any(not char.isalnum() for char in password))
        ):
            self.password = password
            return True
        else:
            return False

    def login(self, password):
        return self.password == password


if __name__ == "__main__":
    usuario = Usuario("pablo", "phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))  # False
    print(usuario.cambiar_password("clavesecreta1_"))  # True
    print(usuario.cambiar_password("clavesecreta"))  # False
    print(usuario.cambiar_password("clasesecreta1"))  # False
    print(usuario.cambiar_password("claveSecreta1"))  # True
    print(usuario.login("clavesecreta1_"))  # True
    print(usuario.login("claveSecreta1"))  # False
           