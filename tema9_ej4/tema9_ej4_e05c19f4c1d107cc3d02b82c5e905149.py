class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        # print(password)
        # print(password != password.upper(), 'and (', password != password.lower(), 'or not', password.isalnum(), ')')
        if 8 <= len(password) <= 16:
            if password != password.upper() and (password != password.lower() or not password.isalnum()):        
                self.password = password
                return True

        return False

    def login(self,password):
        return self.password == password

if __name__ == "__main__":
    usuario=Usuario("pablo","phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))
           
