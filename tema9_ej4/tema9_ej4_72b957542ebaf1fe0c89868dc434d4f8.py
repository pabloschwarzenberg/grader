class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        pass

    def login(self,password):
        pass

if __name__ == "__main__":
    usuario=Usuario("pablo","phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))
           class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.password = ""

    def cambiar_password(self, password):
        if len(password) < 8 or len(password) > 16:
            return False

        has_uppercase = False
        has_special_character = False

        for char in password:
            if char.isupper():
                has_uppercase = True
            elif not char.isalnum():
                has_special_character = True

        if has_uppercase or has_special_character:
            self.password = password
            return True

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
