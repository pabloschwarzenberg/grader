class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.clave = ''

    def cambiar_password(self, password):
        if len(password) < 8 or len(password) > 16:
            return False
        
        has_letter = False
        has_number = False
        has_special = False

        for char in password:
            if char.isalpha() and char.isupper():
                has_letter = True
            elif char.isdigit():
                has_number = True
            elif not char.isalpha() and not char.isdigit():
                has_special = True
        
        if (has_letter or has_special) and has_number:
            self.clave = password
            return True
        else:
            return False

    def login(self, password):
        return self.clave == password
# Crear un objeto Usuario
usuario = Usuario("John Doe", "johndoe@example.com")

# Cambiar la contraseña
password_valida = "Password#123"
password_invalida = "pass123"

if usuario.cambiar_password(password_valida):
    print("Contraseña cambiada exitosamente")
else:
    print("La contraseña no cumple las reglas")

# Verificar el inicio de sesión
if usuario.login(password_valida):
    print("Inicio de sesión exitoso")
else:
    print("Contraseña incorrecta")

if usuario.login(password_invalida):
    print("Inicio de sesión exitoso")
else:
    print("Contraseña incorrecta")
