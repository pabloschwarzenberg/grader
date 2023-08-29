class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.clave = ""
        self.email = email

    def cambiar_password(self, password):
        if len(password) >= 8 and len(password) <= 16:
            has_letter = False
            has_number = False
            has_uppercase = False
            has_special = False

            for char in password:
                if char.isalpha():
                    has_letter = True
                    if char.isupper():
                        has_uppercase = True
                elif char.isdigit():
                    has_number = True
                else:
                    has_special = True

            if (has_letter and has_number) and (has_uppercase or has_special):
                self.clave = password
                return True

        return False

    def login(self, password):
        return self.clave == password

# Ejemplo de uso
usuario = Usuario("JohnDoe", "johndoe@example.com")
print(usuario.nombre)  # Salida: JohnDoe
print(usuario.email)  # Salida: johndoe@example.com

usuario.cambiar_password("Password123")
print(usuario.clave)  # Salida: Password123

print(usuario.login("Password123"))  # Salida: True
print(usuario.login("wrongpassword"))  # Salida: False
