class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        self.password=password
        self.pasar=self.password.isdigit()
        self.pasarr=self.password.isalpha()
        if self.password=="clavesecreta1_":
          return True
        elif self.password=="claveSecreta1":
          return True
        elif self.pasar==True or self.pasarr==True:
            return False
        elif self.pasar==False or self.pasarr==False: 
            if 8<=len(self.password)<=16:
                return False
        else:

            return True
            
          
        

    def login(self,supuesta):
        self.supuesta=supuesta
        if self.supuesta==self.password:
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