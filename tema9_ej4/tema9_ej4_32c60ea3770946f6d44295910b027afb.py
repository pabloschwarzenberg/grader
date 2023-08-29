class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.clave = ""

    def cambiar_password(self, password):
        if len(password) < 8 or len(password) > 16:
            return False
        elif not any(char.isdigit() for char in password):
            return False
        elif not any(char.isalpha() for char in password):
            return False
        elif not any(char.isupper() or not char.isalnum() for char in password):
            return False

        self.clave = password
        return True

    def login(self, password):
        return password == self.clave


if __name__ == "__main__":
    usuario = Usuario("Juan", "juan@example.com")

    print(usuario.cambiar_password("12345678"))  # Salida: False (no cumple longitud mínima)
    print(usuario.cambiar_password("password"))  # Salida: False (no contiene número)
    print(usuario.cambiar_password("passw0rd"))  # Salida: False (no contiene letra mayúscula o carácter especial)
    print(usuario.cambiar_password("Password123"))  # Salida: True (cumple todas las reglas)
    print(usuario.clave)  # Salida: "Password123"

    print(usuario.login("Password123"))  # Salida: True
    print(usuario.login("password"))  # Salida: False
