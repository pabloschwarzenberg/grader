class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        cambia = False
        symbols = "#¿?¡!@$\/&;,:-_"
        hay_simbolo = False
        l = len(password)
        for caracter in password:
            if caracter in symbols:
                hay_simbolo = True
                break
        if l >= 8 and l <= 16:
            if not password.isnumeric() and not password.isalpha():
                if not password.isupper() and not password.islower() or hay_simbolo:
                    cambia = True
                    self.password = password
        return cambia

    def login(self,password):
        if self.password == password:
            return True
        else:
            return False

if __name__ == "__main__":
    usuario=Usuario("pablo","phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))
