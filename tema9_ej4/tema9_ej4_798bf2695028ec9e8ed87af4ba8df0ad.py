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
print("Usuario: {}, Email: {}, Clave: {}".format(usuario.nombre, usuario.email, usuario.clave))

if usuario.cambiar_password("password123"):
    print("Cambio de clave exitoso")
else:
    print("La nueva clave no cumple las reglas")

print("Usuario: {}, Email: {}, Clave: {}".format(usuario.nombre, usuario.email, usuario.clave))

if usuario.login("password123"):
    print("Acceso concedido")
else:
    print("Clave incorrecta")
