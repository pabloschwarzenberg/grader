class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""
        
    def cambiar_password(self,password):
        no=["1","2","3","4","5","6","7","8","9","0"]
        p2=list(password)
        c=-1
        for i in p2:
            c+=1
            if i in no:
                del p2[c]
            else:
                continue

        if "".join(p2).islower()==True and "".join(p2).isalpha()==True:
            cond2=False
        else:
            cond2=True
        
        if len(password)>=8 and len(password)<=16 and cond2==True:
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
           