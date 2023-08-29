class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.clave = ""

    def cambiar_password(self, password):
        # Verificar longitud de la password
        if len(password) < 8 or len(password) > 16:
            return False

        # Verificar si contiene letras y números
        if not any(c.isalpha() for c in password) or not any(c.isdigit() for c in password):
            return False

        # Verificar si contiene al menos una letra mayúscula o un carácter especial
        if not any(c.isupper() for c in password) and not any(not c.isalnum() for c in password):
            return False

        self.clave = password
        return True

    def login(self, password):
        return self.clave == password


# Ejemplo de uso de la clase Usuario
usuario1 = Usuario("John Doe", "john@example.com")
print(usuario1.cambiar_password("password"))  # False, no cumple las reglas de validación
print(usuario1.cambiar_password("password123"))  # False, no contiene letra mayúscula o carácter especial
print(usuario1.cambiar_password("Password123"))  # True, cumple todas las reglas de validación
print(usuario1.login("Password123"))  # True, la password ingresada es correcta
print(usuario1.login("password"))  # False, la password ingresada es incorrecta
