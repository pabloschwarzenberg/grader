from string import punctuation

list1 = list(punctuation)
class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.password = ""

    def cambiar_password(self, password):
        if 8 <= len(password) <= 16 and any(i.isalpha() for i in password) and any(i.isdigit() for i in password) and (any(i.isupper() for i in password) or any(i == j for i in password for j in list1)):
            self.password = password
            return True

        else:
            return False

    def login(self, password):
        if self.password == password:
            return True
        else:
            return False


if __name__ == "__main__":
    usuario = Usuario("pablo", "phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))

