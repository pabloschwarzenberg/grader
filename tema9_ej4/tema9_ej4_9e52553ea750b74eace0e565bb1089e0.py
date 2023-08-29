class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.clave = ""

    def cambiar_password(self, password):
        if len(password) < 8 or len(password) > 16:
            return False
        
        tiene_letras_numeros = any(char.isalpha() or char.isdigit() for char in password)
        tiene_mayuscula_o_especial = any(char.isupper() or not char.isalnum() for char in password)
        
        if not tiene_letras_numeros or not tiene_mayuscula_o_especial:
            return False
        
        self.clave = password
        return True

    def login(self, password):
        return self.clave == password

# Ejemplo de uso
usuario = Usuario("JohnDoe", "johndoe@example.com")
print(usuario.nombre)  # Salida: JohnDoe
print(usuario.email)  # Salida: johndoe@example.com

# Cambiar la contraseña
if usuario.cambiar_password("P@ssw0rd"):
    print("Contraseña actualizada correctamente.")
else:
    print("La contraseña no cumple las reglas.")

# Iniciar sesión
if usuario.login("P@ssw0rd"):
    print("Inicio de sesión exitoso.")
else:
    print("La contraseña no coincide.")

   
           