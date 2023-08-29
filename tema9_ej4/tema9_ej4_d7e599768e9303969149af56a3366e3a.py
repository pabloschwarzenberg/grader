class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.clave = ''

    def cambiar_password(self, password):
        if 8 <= len(password) <= 16:
            if any(char.isupper() or not char.isalnum() for char in password):
                self.clave = password
                return True
        return False

    def login(self, password):
        return self.clave == password


# Ejemplo de uso
usuario = Usuario('John Doe', 'john@example.com')
usuario.cambiar_password('Abcdef123#')
print(usuario.login('Abcdef123#'))  # True
print(usuario.login('password'))  # False