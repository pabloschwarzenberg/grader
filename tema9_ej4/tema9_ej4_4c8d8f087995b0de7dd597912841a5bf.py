class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.clave = ""

    def cambiar_password(self, password):
        if 8 <= len(password) <= 16:
            if any(char.isupper() or not char.isalnum() for char in password):
                self.clave = password
                return True
        return False

    def login(self, password):
        return password == self.clave

# Ejemplo de uso
usuario = Usuario("John", "john@example.com")

# Cambiar la contraseña
if usuario.cambiar_password("password123"):
    print("Contraseña cambiada con éxito")
else:
    print("La contraseña no cumple con los requisitos")

# Iniciar sesión
if usuario.login("password123"):
    print("Inicio de sesión exitoso")
else:
    print("Inicio de sesión fallido")
