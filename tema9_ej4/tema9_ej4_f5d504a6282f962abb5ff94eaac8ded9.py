class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.clave = ""
        self.email = email

    def cambiar_password(self, password):
        if len(password) < 8 or len(password) > 16:
            return False

        tiene_letras_numeros = any(char.isalpha() or char.isdigit() for char in password)
        tiene_mayuscula_o_caracter_especial = any(
            char.isupper() or not char.isalnum() for char in password
        )

        if not tiene_letras_numeros or not tiene_mayuscula_o_caracter_especial:
            return False

        self.clave = password
        return True

    def login(self, password):
        return self.clave == password
