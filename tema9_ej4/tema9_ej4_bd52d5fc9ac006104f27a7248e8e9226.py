class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.password = ""

    def cambiar_password(self, password):
        lista_numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        mayusculas = "QWERTYUIOPASDFGHJKLÑZXCVBNM"
        lista_mayusculas = []
        lista_caracteres = ["!", "$", "=", "?", "¡", "¿", "*", "+", "}", "{", "&", "-","_"]

        for letra in mayusculas:
            lista_mayusculas.append(letra)
        numero = False
        for i in password:
            if i in lista_numeros:
                numero = True
        largo = False
        if 8 <= len(password) <= 16:
            largo = True
        mayusculas = False
        for i in password:
            if i in lista_mayusculas:
                mayusculas = True
        caracteres = False
        for i in password:
            if i in lista_caracteres:
                caracteres = True

        if numero and (mayusculas or caracteres):
            self.password = password
            return True
        else:
            return False


    def login(self, password):
        if password == self.password:
            return True
        else:
            return False


if __name__ == "__main__":
    usuario = Usuario("pablo", "phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))
