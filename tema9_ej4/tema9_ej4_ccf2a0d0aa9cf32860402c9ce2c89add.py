class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.clave = ''

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
usuario = Usuario("John Doe", "johndoe@example.com")
print(usuario.nombre)  # Imprime "John Doe"
print(usuario.email)  # Imprime "johndoe@example.com"

usuario.cambiar_password("pass123")
print(usuario.clave)  # Imprime "pass123"

if usuario.login("pass123"):
    print("Inicio de sesión exitoso")
else:
    print("Inicio de sesión fallido")

           