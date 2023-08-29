class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.password = ""
   
    def cambiar_password(self, password):
        if self.validar_password(password):
            self.password = password
            return True
        else:
            return False 
    
    def validar_password(self, password):
        if len(password) < 8 or len(password) > 16:
            return False 
           
        tiene_letras_numeros = any(char.isalpha() or char.isdigit() for char in password) 
        tiene_mayuscula_o_caracter_especial = any(char.isupper() or not char.isalnum() for char in password)
        
        return tiene_letras_numeros and tiene_mayuscula_o_caracter_especial
        
    def login(self, password):
        return self.password == password 


if __name__ == "__main__":
    usuario = Usuario("tomas vargas", "tomasvargas@ejemplo.com")
    print(usuario.cambiar_password("password"))
    print(usuario.cambiar_password("passwrod1"))
    print(usuario.login("password1"))
    print(usuario.login("incorrectpassword"))
