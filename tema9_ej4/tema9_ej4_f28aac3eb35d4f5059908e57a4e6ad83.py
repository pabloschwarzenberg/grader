class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.clave = ""

    def cambiar_password(self, password):
        if len(password) < 8 or len(password) > 16:
            return False
        elif not any(char.isupper() or not char.isalpha() for char in password):
            return False
        elif not any(not char.isalnum() or char.isalpha() for char in password):
            return False
        else:
            self.clave = password
            return True

    def login(self, password):
        return self.clave == password


# Ejemplo de uso
usuario = Usuario("usuario1", "usuario1@example.com")
print(usuario.nombre)  # Salida: usuario1
print(usuario.email)  # Salida: usuario1@example.com

usuario.cambiar_password("Password1#")
print(usuario.clave)  # Salida: Password1#

print(usuario.login("Password1#"))  # Salida: True
print(usuario.login("otraclave"))  # Salida: False          