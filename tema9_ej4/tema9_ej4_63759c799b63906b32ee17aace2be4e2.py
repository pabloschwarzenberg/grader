class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        if  8 <= len(self.password) <= 16:
            numeros = list("123456789")
            palabrasM = list("ABCDEFGHIJKLMNOPQ")
            palabras = list("abcdefghijklmnopq")
            c=0
            h = list(self.password)
            for i in range(len(self.password)):
                if self.password.find(numeros[i])!= -1:
                    h.remove(numeros[i])
                    c = c + 1
            if c != 0:
                k = 0
                for j in range(len(self.password)):
                    while str(h).find(palabras[j]) != -1:
                        h.remove(palabras[j])
                        k = k + 1
                if k != 0:
                    p = 0
                    for o in range(len(self.password)):
                        while str(h).find(palabrasM[o]) != -1:
                            h.remove(palabrasM[o])
                            p = p + 1
                        if p != 0:
                            if len(h)!=0:
                                return True
        else:
            return False





    def login(self,password):
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