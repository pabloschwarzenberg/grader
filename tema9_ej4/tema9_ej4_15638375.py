
class Usuario():
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.password = ''

    def cambiar_password(self, password):
        numeros = []
        if len(password) < 8 or len(password) > 16:
            return False
        elif password.find('_') == -1 and password.find('S') == -1:
            return False
        else:
            for letra in password:
                try:
                    numero = int(letra)
                    numeros.append(numero)
                except:
                    pass
        print (numeros)
        if len(numeros) == 0:
            return False
        else:
            self.password = password
            return True

    def login(self, password):
        if password == self.password:
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
           