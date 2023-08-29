class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.clave = ""

    def cambiar_password(self, password):
        if len(password) >= 8 and len(password) <= 16:
            if any(c.isupper() or not c.isalnum() for c in password):
                self.clave = password
                return True
        return False

    def login(self, password):
        return password == self.clave


if __name__ == "__main__":
    usuario = Usuario("ejemplo", "ejemplo@example.com")

    # Cambiar la contraseña
    nueva_password = input("Ingresa una nueva contraseña: ")
    if usuario.cambiar_password(nueva_password):
        print("Contraseña cambiada con éxito")
    else:
        print("La contraseña no cumple las reglas")

    # Iniciar sesión
    password_ingresada = input("Ingresa tu contraseña para iniciar sesión: ")
    if usuario.login(password_ingresada):
        print("Inicio de sesión exitoso")
    else:
        print("Contraseña incorrecta")