class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.clave = ""

    def cambiar_password(self, password):
        if len(password) >= 8 and len(password) <= 16:
            tiene_letras_numeros = any(char.isalpha() or char.isdigit() for char in password)
            tiene_mayuscula_o_caracter = any(char.isupper() or not char.isalnum() for char in password)
            if tiene_letras_numeros and tiene_mayuscula_o_caracter:
                self.clave = password
                return True
        return False

    def login(self, password):
        return self.clave == password
