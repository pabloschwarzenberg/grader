class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.password = ""

    def cambiar_password(self, password):
        numeros='0123456789'
        letras='abcdefghijklmnñopqrstuvwxyz'
        password_lower = password.lower()
        i = 0
        numero = False
        letra = False
        caracter_especial = False

        if 8<=len(password)<=16:
            while i < len(password):
                if password_lower[i] in numeros:
                    numero = True
                if password_lower[i] in letras:
                    letra = True
                if (password[i] not in numeros) and (password[i] not in letras):
                    caracter_especial = True
                if numero and letra and caracter_especial:
                    self.password=password
                    return True
                i = i + 1
            return False
        else:
            return False

    def login(self, password):
        if password==self.password:
            return True
        else:
            return False

if __name__ == "__main__":
    usuario=Usuario("pablo","phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))
           