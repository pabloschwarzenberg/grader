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
        self.email = email
        self.clave = ""

    def cambiar_password(self, password):
        if len(password) < 8 or len(password) > 16:
            return False
        if not any(char.isalpha() for char in password) or not any(char.isdigit() for char in password):
            return False
        if not any(char.isupper() or not char.isalnum() for char in password):
            return False

        self.clave = password
        return True

    def login(self, password):
        return self.clave == password

# Ejemplo de uso
usuario = Usuario("John Doe", "johndoe@example.com")

# Cambiar la password
if usuario.cambiar_password("abc123XYZ"):
    print("Password cambiada exitosamente.")
else:
    print("La password no cumple con las reglas.")

# Iniciar sesión
if usuario.login("abc123XYZ"):
    print("Inicio de sesión exitoso.")
else:
    print("La password ingresada es incorrecta.")
          