class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.clave = ""

    def cambiar_password(self, password):
        if len(password) < 8 or len(password) > 16:
            return False

        tiene_letras_numeros = any(c.isalpha() or c.isdigit() for c in password)
        tiene_mayuscula_o_especial = any(c.isupper() or not c.isalnum() for c in password)

        if tiene_letras_numeros and tiene_mayuscula_o_especial:
            self.clave = password
            return True
        else:
            return False

    def login(self, password):
        return self.clave == password

           