class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.clave = ''

    def cambiar_password(self, password):
        if len(password) >= 8 and len(password) <= 16:
            if any(char.isupper() or not char.isalnum() for char in password):
                self.clave = password
                return True
        return False

    def login(self, password):
        return self.clave == password

usuario = Usuario("John Doe", "johndoe@example.com")

usuario.cambiar_password("abc123")  # False, no cumple la longitud mínima
usuario.cambiar_password("passw0rd")  # False, no contiene una letra mayúscula o un carácter especial
usuario.cambiar_password("Password1!")  # True, cumple todas las reglas y se actualiza la clave

usuario.login("Password1!")  # True, la contraseña ingresada coincide
usuario.login("abc123")  # False, la contraseña ingresada no coincide
