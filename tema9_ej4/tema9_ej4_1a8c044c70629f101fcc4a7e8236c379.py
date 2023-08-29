class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.clave = ""
        self.email = email

    def cambiar_password(self, password):
        if len(password) < 8 or len(password) > 16:
            return False
        if not any(char.isdigit() for char in password):
            return False
        if not any(char.isalpha() for char in password):
            return False
        if not any(char.isupper() or not char.isalnum() for char in password):
            return False

        self.clave = password
        return True

    def login(self, password):
        return self.clave == password


# Ejemplo de uso
usuario = Usuario("JohnDoe", "johndoe@example.com")
print(usuario.nombre)  # Output: JohnDoe
print(usuario.email)  # Output: johndoe@example.com
print(usuario.clave)  # Output: ""

usuario.cambiar_password("password123")
print(usuario.clave)  # Output: password123

print(usuario.login("password123"))  # Output: True
print(usuario.login("incorrect_password"))  # Output: False
