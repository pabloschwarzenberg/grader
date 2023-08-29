class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.clave = ""

    def cambiar_password(self, password):
        if len(password) >= 8 and len(password) <= 16:
            if any(c.isupper() for c in password) or any(c in "!@#$%^&*()-_=+[{]}\|;:'\",<.>/?`~" for c in password):
                self.clave = password
                return True
        return False

    def login(self, password):
        return self.clave == password

if __name__ == "__main__":
    usuario = Usuario("JohnDoe", "johndoe@example.com")

    # Cambiar la password
    if usuario.cambiar_password("Password1"):
        print("Password cambiada con éxito")
    else:
        print("La password no cumple las reglas")

    # Intentar iniciar sesión
    if usuario.login("Password1"):
        print("Inicio de sesión exitoso")
    else:
        print("Inicio de sesión fallido")
