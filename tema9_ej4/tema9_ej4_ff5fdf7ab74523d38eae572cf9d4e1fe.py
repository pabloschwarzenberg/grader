class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        abc123="abcdefghijklmnopqrstuvwxyz1234567890"
        kk="ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%ˆ&*()_+=-`˜`"
        if len(password)>7 and len(password)<17:
            ñe=list(password)
            i=0
            while i<len(ñe):
                if ñe[i] in kk:
                    self.password=password
                    return True
                else:
                    i+=1
            return False
        else:
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
           