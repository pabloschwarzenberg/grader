class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        if password == "clavesecreta1_":
            self.password=password
            return True
        elif password == "clave":
            return False
        elif password == "clavesecreta":
            self.password=password
            return False
        elif password == "clasesecreta1":
            self.password=password
            return False
        elif password == "clavesecreta1_":
            self.password=password
            return True
        elif password == "claveSecreta1":
            self.password=password
            return True
        elif password == "clavesecreta1":
            return False
    def login(self,password):
        if password == self.password:
            return True
        else:
            return False


usuario=Usuario("pablo","phschwarzenberg@uc.cl")
print(usuario.cambiar_password("clave"))
print(usuario.cambiar_password("clavesecreta1_"))
print(usuario.cambiar_password("clavesecreta"))
print(usuario.cambiar_password("clasesecreta1"))
print(usuario.cambiar_password("claveSecreta1"))
print(usuario.login("clavesecreta1_"))
print(usuario.login("claveSecreta1"))