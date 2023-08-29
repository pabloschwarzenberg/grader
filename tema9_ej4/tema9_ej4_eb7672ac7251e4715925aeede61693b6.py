import string
class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.password = ""

    def cambiar_password(self, password):
        signos="_#$%&()="
        contadorM=0
        contadorW=0
        contadorN=0
        if 8<=len(password)<=16:
            for i in password:
                if i.isdigit()==True:
                    contadorN+=1
                if i in string.ascii_uppercase:
                    contadorM+=1
                if i in signos:
                    contadorW+=1
            print(contadorM)
            print(contadorW)
            if contadorM >= 1 and contadorN >=1 or contadorW >=1 and contadorN>=1:
                self.password = password
                return True
            else:
                return False
        else:
            return False
        pass
    def login(self, password):
        if password==self.password:
            return True
        else:
            return False
        pass



if __name__ == "__main__":
    usuario = Usuario("pablo", "phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))
