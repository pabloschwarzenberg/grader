class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.clave = ""
        self.email = email

    def cambiar_password(self, password):
        if len(password) < 8 or len(password) > 16:
            return False

        if not any(char.isupper() or not char.isalnum() for char in password):
            return False

        self.clave = password
        return True

    def login(self, password):
        return self.clave == password


# Ejemplo de uso
usuario = Usuario("JohnDoe", "johndoe@example.com")
print(usuario.nombre)  # JohnDoe
print(usuario.email)  # johndoe@example.com
print(usuario.clave)  # ""

usuario.cambiar_password("Abc12345")
print(usuario.clave)  # Abc12345

print(usuario.login("Abc12345"))  # True
print(usuario.login("incorrect_password"))  # False
           