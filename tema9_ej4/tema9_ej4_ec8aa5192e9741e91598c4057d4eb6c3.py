class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.clave = ""

    def cambiar_password(self, password):
        if 8 <= len(password) <= 16 and any(char.isalpha() and char.isupper() or not char.isalnum() for char in password):
            self.clave = password
            return True
        return False

    def login(self, password):
        return password == self.clave


# Ejemplo de uso
if __name__ == "__main__":
    usuario = Usuario("John", "john@example.com")
    print(usuario.cambiar_password("password123"))  # True
    print(usuario.clave)  # "password123"
    print(usuario.login("password123"))  # True
    print(usuario.login("clavesecreta1"))  # False
