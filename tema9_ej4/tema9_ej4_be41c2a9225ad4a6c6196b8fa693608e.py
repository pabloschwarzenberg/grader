class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.clave = ""

    def cambiar_password(self, password):
        if len(password) >= 8 and len(password) <= 16:
            if any(char.isupper() for char in password) or any(not char.isalnum() for char in password):
                self.clave = password
                return True
        return False

    def login(self, password):
        return password == self.clave
usuario = Usuario("JohnDoe", "johndoe@example.com")
print(usuario.nombre)  
print(usuario.email) 
print(usuario.clave)  

usuario.cambiar_password("abcd1234")
print(usuario.clave)   
usuario.cambiar_password("SecurePassword#123")
print(usuario.clave) 

print(usuario.login("WrongPassword"))           
print(usuario.login("SecurePassword#123"))       
