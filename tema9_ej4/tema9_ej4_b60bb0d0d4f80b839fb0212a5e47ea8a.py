class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        if len(password)>=8:
            for i in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ!·#$¢%∞&¬/“)”=≠?´¿‚^[*{¨Ç}_–":
                if i in password:
                    for r in "1234567890":
                        if r in password:
                            self.paswword=password
                            return True
        return False
                    
            

    def login(self,password):
        if password==self.password:
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
           