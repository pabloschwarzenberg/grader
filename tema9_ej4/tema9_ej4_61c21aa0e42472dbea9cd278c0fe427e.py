class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.password = ""

    def cambiar_password(self, password):
        if 8 <= len(password) <= 16:
            if password.replace('_','').isalnum():
                if '_' in password:
                    self.password = password
                    return True
                for i in password:
                    if i in 'ABCDEFGHIJKMNLÑOPQRSTUVWXYZ':
                        self.password = password
                        return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def login(self, password):
        if password == self.password:
            return True
        else:
            return False


if __name__ == "__main__":
    usuario = Usuario("pablo", "phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_")) # Si password = clavesecreta1_ el resultado debiera ser True
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))  # Si password = clavesecreta1_ el resultado debiera ser False
    print(usuario.cambiar_password("claveSecreta1"))  # Si password = claveSecreta1 el resultado debiera ser True
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))
