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
usuario = Usuario("ejemplo", "ejemplo@example.com")
print(usuario.cambiar_password("password123"))  # True
print(usuario.cambiar_password("12345678"))  # False
print(usuario.login("password123"))  # True
print(usuario.login("incorrecta"))  # False
           