class Usuario:
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
    print(usuario.login("claveSecreta1"))
import re

class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.clave = ''

    def cambiar_password(self, password):
        if self.validar_password(password):
            self.clave = password
            return True
        else:
            return False

    def login(self, password):
        return self.clave == password

    def validar_password(self, password):
        if 8 <= len(password) <= 16:
            if re.search(r'[a-zA-Z0-9]', password):
                if re.search(r'[A-Z!@#$%^&*(),.?":{}|<>]', password):
                    return True
        return False


# Ejemplo de uso
usuario1 = Usuario("JohnDoe", "johndoe@example.com")

print(usuario1.cambiar_password("password"))  # Output: False
print(usuario1.cambiar_password("StrongP@ssw0rd"))  # Output: True
print(usuario1.login("password"))  # Output: False
print(usuario1.login("StrongP@ssw0rd"))  # Output: True
