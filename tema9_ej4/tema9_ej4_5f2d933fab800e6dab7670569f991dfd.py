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
        return password == self.password

    def validar_password(self, password):
        if len(password) < 8 or len(password) > 16:
            return False

        tiene_letras_numeros = any(c.isalpha() or c.isdigit() for c in password)
        tiene_mayuscula_o_especial = any(c.isupper() or not c.isalnum() for c in password)

        return tiene_letras_numeros and tiene_mayuscula_o_especial


if __name__ == "__main__":
    usuario = Usuario("pablo", "phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))

           