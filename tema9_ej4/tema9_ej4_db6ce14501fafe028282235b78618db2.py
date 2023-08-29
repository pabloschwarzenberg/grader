class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.password = ""

    def cambiar_password(self, password):
        if len(password) < 8 or len(password) > 16:
            return False

        tiene_letras_numeros = any(char.isalpha() or char.isdigit() for char in password)
        tiene_mayuscula_o_especial = any(char.isupper() or not char.isalnum() for char in password)

        if not tiene_letras_numeros or not tiene_mayuscula_o_especial:
            return False

        self.password = password
        return True

    def login(self, password):
        return self.password == password


if __name__ == "__main__":
    usuario = Usuario("pablo", "phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))