class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        clave = password
        if ((len(clave) <= 16) and (len(clave) >= 8)):
            letras = 0
            numeros = 0
            for i in clave:
                if i.isalpha() == True:
                    letras += 1
            for i in clave:
                if i.isnumeric() == True:
                    numeros += 1
            if (letras > 0) and (numeros > 0):
                if (letras + numeros) < len(clave):
                    self.password = clave
                    return True
                elif clave != clave.lower():
                    self.password = clave
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def login(self,password):
        if self.password == password:
            return True
        else:
            return False

        pass

if __name__ == "__main__":
    usuario=Usuario("pablo","phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))
           