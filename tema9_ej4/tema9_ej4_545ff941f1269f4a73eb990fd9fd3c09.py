class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""
    def password_valida(self,password):
        valida=False
        v1=False
        v2=False
        for i in password:
            if i in 'ABCDEFGHIJKLMÑNOPQRSTUVWXYZ'or not i in 'abcdefghijklmñnopqrstuvwxyz1234567890':
                v1=True
        if len(password)<17 and len(password)>7:
            v2=True
        if v1==True and v2==True:
            valida=True
        return valida
    def cambiar_password(self,password):
        if self.password_valida(password)==True:
            return True
        else:
            return False
    def login(self,clave):
        if clave==self.password:
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
