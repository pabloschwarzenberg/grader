class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.clave = ""

    def cambiar_password(self, password):
        if len(password) < 8 or len(password) > 16:
            return False

        has_letter = False
        has_number = False
        has_uppercase = False
        has_special_char = False

        for char in password:
            if char.isalpha():
                has_letter = True
                if char.isupper():
                    has_uppercase = True
            elif char.isdigit():
                has_number = True
            else:
                has_special_char = True

        if (has_letter and has_number) and (has_uppercase or has_special_char):
            self.clave = password
            return True
        else:
            return False

    def login(self, password):
        return self.clave == password


# Ejemplo de uso de la clase Usuario

usuario = Usuario("JohnDoe", "johndoe@example.com")
print(usuario.cambiar_password("pass123"))  # False, no cumple las reglas de contraseña
print(usuario.cambiar_password("password123"))  # False, no contiene carácter especial
print(usuario.cambiar_password("Password123"))  # True, cumple todas las reglas de contraseña
print(usuario.login("Password123"))  # True, la contraseña ingresada coincide con la del usuario
print(usuario.login("incorrectpassword"))  # False, la contraseña ingresada no coincide con la del usuario