class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.clave = ""
        self.email = email

    def validacion_char(self, string):
        letras = False
        numeros = False
        especial = False
        mayuscula = False

        for char in string:
            if char.isalpha():
                letras = True
                if char.isupper():
                    mayuscula = True
            elif char.isdigit():
                numeros = True
            else:
                especial = True

        if letras == True and numeros == True and (especial == True or mayuscula == True):
            return True
        else:
            return False
        

    def cambiar_password(self, password):
        caracteres = self.validacion_char(password)
        if (8 <= len(password) <= 16) and caracteres == True:
            self.clave = password
            return True
        else:
            return False
        
    def login(self,password):
        if self.clave == password:
            return True
        else:
            return False           