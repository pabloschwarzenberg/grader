class Usuario:
    def __init__(self,nombre,email):
        self.nombre = nombre
        self.clave = ""
        self.email = email

    def cambiar_password(self,password):
        l = list(password)
        if len(l) >= 8 and len(l) <= 16:
            letra = False
            numeros = False
            mayuscula = False
            simbolo = False
            a = password.lower()
            b = password.isalpha()
            if a != password:
                mayuscula = True
            for i in range(len(l)):
                if l[i].isalpha() == True:
                    letra  = True
                if l[i].isnumeric() == True:
                    numeros = True
                if l[i].isalpha() == False and l[i].isnumeric() == False:
                    simbolo = True
            if (letra == True and numeros == True and  mayuscula == True) or (letra == True and numeros == True and  simbolo == True):
                self.clave = password
                return True
            else:
                return False
        else:
            return False
    def login(self,password):
        if self.clave == password:
            return True
        else:
            return False

usuario = Usuario("matias","msarellano@uc.cl")
print(usuario.cambiar_password("clave"))
print(usuario.cambiar_password("clavesecreta1_"))
print(usuario.login("clavesecreta1_"))

if __name__ == "__main__":
    usuario=Usuario("pablo","phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))
           