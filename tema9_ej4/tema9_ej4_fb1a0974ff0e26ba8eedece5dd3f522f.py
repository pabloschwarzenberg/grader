class Usuario:
    def __init__(self,nombre,email):
        self.usuario = nombre
        self.clave = ""
        self.email = email

    def cambiar_password(self,clave):
        hashtag = False
        for i in clave:
            if not i.isnumeric() and not i.isalpha():
                hashtag = True
        numero = False
        for i in clave:
            if i.isnumeric():
                numero = True

        letra = False
        for i in clave:
            if i.isalpha():
                letra = True
        
        if 7 <= len(clave) <= 15 and letra and numero and (clave != clave.lower() or hashtag):
            self.clave = clave
            return True
        else:
            return False
            

    def login(self,password):
        if password == self.clave:
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


           