letras = "abcdefghijklmnopqrstuvwxyz"
simbolos = "_:;/&"


class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.password = ""

    def cambiar_password(self, password):
        if 8 < len(password) < 16:
            i = 0
            for letra in password:
                if letra.isnumeric:
                    i = i + 1
                else:
                    i = i
                for letriwi in password:
                    if letriwi.isupper() or letriwi in simbolos:
                        i = i + 1
                if i == 2:
                    return True
                else:
                    return False

        else:
            return False


    def login(self, password):
        if self.password == self.cambiar_password(password):
            return True
        else:
            return False
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