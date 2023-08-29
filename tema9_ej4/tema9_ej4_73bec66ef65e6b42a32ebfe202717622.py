class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def clave_valida(self, password):
        if len(password)>7 and len(password)<17:
            letras="abcdefghijklmnopqrstuvwxyz"
            minusculas=list(letras)
            mayusculas = list(letras.upper())
            numeros="0123456789"
            numeros=list(numeros)
            for i in password:
                if i in minusculas:
                    continue
                elif i in numeros:
                    continue
                else:
                    return True
        return False

    def cambiar_password(self,password):
        if Usuario(self.nombre,self.email).clave_valida(password)==True:
            self.password=password
            return True
        else:
            return False
        

    def login(self,password):
        if self.password==password:
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
