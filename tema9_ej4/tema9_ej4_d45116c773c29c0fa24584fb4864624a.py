class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self, password):
        if len(password) < 8 or len(password) > 16:
            return False
        if not any(c.isalpha() for c in password) or not any(c.isdigit() for c in password):
            return False
        if not any(c.isupper() or not c.isalnum() for c in password):
            return False

        self.clave = password
        return True

    def login(self, password):
        return password == self.clave
 
if __name__ == "__main__":
    usuario=Usuario("pablo","phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))
           