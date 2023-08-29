class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.clave = ""

    def cambiar_password(self, password):
        if len(password) >= 8 and len(password) <= 16:
            has_letter = False
            has_number = False
            has_special_char = False

            for char in password:
                if char.isalpha() and char.isupper():
                    has_letter = True
                elif char.isdigit():
                    has_number = True
                elif not char.isalnum():
                    has_special_char = True

            if (has_letter or has_special_char) and has_number:
                self.clave = password
                return True

        return False

    def login(self, password):
        return self.clave == password


# Ejemplo de uso
usuario = Usuario("ejemplo", "ejemplo@example.com")

# Cambiar la contraseña
password_nueva = input("Ingrese la nueva contraseña: ")
if usuario.cambiar_password(password_nueva):
    print("Contraseña cambiada correctamente")
else:
    print("La contraseña no cumple con los requisitos")

# Intentar hacer login
password_ingresada = input("Ingrese su contraseña: ")
if usuario.login(password_ingresada):
    print("¡Inicio de sesión exitoso!")
else:
    print("La contraseña ingresada es incorrecta")
