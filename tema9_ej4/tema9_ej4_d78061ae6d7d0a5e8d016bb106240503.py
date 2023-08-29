class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.clave = ""

    def cambiar_password(self, password):
        if len(password) < 8 or len(password) > 16:
            return False
        
        has_uppercase = any(char.isupper() for char in password)
        has_special_char = any(not char.isalnum() for char in password)

        if not has_uppercase and not has_special_char:
            return False
        
        self.clave = password
        return True

    def login(self, password):
        return self.clave == password

# Crear un usuario
usuario = Usuario("JohnDoe", "johndoe@example.com")

# Cambiar la contraseña
if usuario.cambiar_password("NewPass123"):
    print("Contraseña cambiada exitosamente")
else:
    print("La nueva contraseña no cumple con las reglas")

# Iniciar sesión
if usuario.login("NewPass123"):
    print("Inicio de sesión exitoso")
else:
    print("Contraseña incorrecta")

