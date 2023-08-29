
class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.password = ""

    def cambiar_password(self, password):
        self.password = cambiar_password


    def login(self, password):
        self.password = login

cambiar_password = ""
login = ""

usuario = Usuario("pablo", "phschwarzenberg@uc.cl")

password = usuario.cambiar_password("clavesecreta1_")
print(usuario.cambiar_password("clave"))
print(usuario.cambiar_password("clavesecreta1_"))
print(usuario.cambiar_password("clavesecreta"))
print(usuario.cambiar_password("clasesecreta1"))
print(usuario.cambiar_password("claveSecreta1"))

login = usuario.login("claveSecreta1")


if login == "clavesecreta1_":

    print(usuario.login("claveSecreta1"))




           