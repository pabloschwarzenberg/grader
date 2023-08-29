import re

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

    def validar_password(self, password):
        if 8 <= len(password) <= 16:
            if re.search(r'[A-Z]', password) or re.search(r'[^a-zA-Z0-9]', password):
                return True
        return False

    def login(self, password):
        return self.password == password


if __name__ == "__main__":
    usuario = Usuario("pablo", "phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))  
    print(usuario.cambiar_password("clavesecreta1_"))  
    print(usuario.cambiar_password("clavesecreta"))  
    print(usuario.cambiar_password("clasesecreta1"))  
    print(usuario.cambiar_password("claveSecreta1"))  
    print(usuario.login("clavesecreta1_"))  
    print(usuario.login("claveSecreta1"))     


"""class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        pass

    def login(self,password):
        pass

if __name__ == "__main__":
    usuario=Usuario("pablo","phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))"""
    