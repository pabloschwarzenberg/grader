class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.password = ''

    def cambiar_password(self, password):
        simbolos = ['<', ',', '>', '@', '!','#','$','%','^','&','*','(',')','_','+','[',']',
                    '{','}','?',':',';','|','.','/','~','`','-','=']
        numeros = '1,2,3,4,5,6,7,8,9,0'
        checkNumero = False
        checkMayus = False
        checkSim = False

        if 8 > len(password) or 16 < len(password):
            return False

        for x in password:
            if x in numeros:
                checkNumero = True
            if x.isupper():
                checkMayus = True
            if x in simbolos:
                checkSim = True

        if checkNumero and (checkMayus or checkSim):
            self.password = password
            return True

        return False

    def login(self, password):
        if password == self.password:
            return True
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
