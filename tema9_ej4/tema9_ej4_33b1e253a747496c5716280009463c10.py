class Usuario():
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.password = ""

    def cambiar_password(self, password):
        valida = True
        if not (len(password) >= 8 and len(password) <= 16):
            valida = False

        numeros = 0
        letras = 0
        for caracter in password:
            if caracter.isdigit():
                numeros += 1
            if caracter.isalpha():
                letras += 1
        
        if numeros == 0 or letras == 0:
            valida = False

        mayusculas = 0
        caracteres_especiales = 0
        for caracter in password:
            if caracter.isupper():
                mayusculas += 1
            if not caracter.isalnum():
                caracteres_especiales += 1

        if mayusculas == 0 and caracteres_especiales == 0:
            valida = False

        if valida:
            self.clave = password
            return True
        else:
            return False

    def login(self, password):
        if password == self.password:
            return True
        else:
            return False

if __name__ == "__main__":
    # Ejemplo de uso
    usuario = Usuario("pablo", "phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))