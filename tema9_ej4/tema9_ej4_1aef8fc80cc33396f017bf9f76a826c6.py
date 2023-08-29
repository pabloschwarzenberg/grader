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

    def validar_password(self, password):
        if len(password) < 8 or len(password) > 16:
            return False
        if not any(char.isupper() or not char.isalnum() for char in password):
            return False
        return True

    def login(self, password):
        return password == self.clave

if __name__ == "__main__":
    usuario = Usuario("JohnDoe", "johndoe@example.com")
    print(usuario.cambiar_password("Abc123#"))  # True
    print(usuario.login("Abc123#"))  # True
    print(usuario.login("wrongpassword"))  # False
