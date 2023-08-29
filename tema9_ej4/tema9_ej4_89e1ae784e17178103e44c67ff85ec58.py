
import re
class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.password = ""

    def cambiar_password(self, password):
        letra=False
        largo=False
        mayu=False
        numero=False
        especial=False
        if 8 <= len(password) <= 16:
            largo=True
        else:
            largo=False
        for i in password:
            if i.isalpha():
                letra=True
                if len(re.sub('[^A-Z]', '', password))>=1:
                    mayu=True
            elif i.isdigit():
                numero=True
            else:
                especial=True
        if largo and letra and numero and (mayu or especial):
            self.password=password
            return True
        else:
            return False

    pass

    def login(self, password):
        if self.password==password:
            return True
        else:
            return False
        pass


if __name__ == "__main__":
    usuario = Usuario("pablo", "phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))
