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
class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.clave = ""
        self.email = email

    def cambiar_password(self, password):
        # Validar las reglas de la password
        if len(password) < 8 or len(password) > 16:
            return False

        if not any(char.isalpha() for char in password) or not any(char.isdigit() for char in password):
            return False

        if not any(char.isupper() for char in password) and not any(char in "!@#$%^&*()-_=+[]{};:'\"|\\<>,.?/" for char in password):
            return False

        # La password cumple con las reglas, se actualiza el atributo clave
        self.clave = password
        return True

    def login(self, password):
        # Verificar si la password ingresada coincide con la clave del usuario
        return password == self.clave
usuario = Usuario("ejemplo", "ejemplo@example.com")
usuario.cambiar_password("Password123!")
print(usuario.clave)  # Imprime la nueva clave establecida

logueado = usuario.login("Password123!")
print(logueado)  # Imprime True si la password coincide, False de lo contrario
           