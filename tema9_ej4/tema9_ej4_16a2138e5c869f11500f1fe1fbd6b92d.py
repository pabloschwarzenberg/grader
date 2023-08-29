class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.clave = ''
    
    def cambiar_password(self, password):
        if len(password) < 8 or len(password) > 16:
            return False
        
        tiene_letras_numeros = any(c.isalpha() or c.isdigit() for c in password)
        tiene_mayuscula_o_caracter = any(c.isupper() or not c.isalnum() for c in password)
        
        if not (tiene_letras_numeros and tiene_mayuscula_o_caracter):
            return False
        
        self.clave = password
        return True
    
    def login(self, password):
        return self.clave == password
