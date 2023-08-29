class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        self.password=""
        self.password+= password
        n= 0
        m= 0
        p= 0
        c= 0
        for i in self.password:
            if i=="0" or i=="1" or i=="2" or i=="3" or i=="4" or i=="5" or i=="6" or i=="7" or i=="8" or i=="9":
                n+=1
            if i >= 'A' and i <= 'Z':
                m+=1
            if i.isalnum()==True:
                p=p+1
        c= len(self.password)-p

        if 8<len(self.password)<16 and n!=0 and p!=0 and (m!=0 or c!=0):
            return True
        else:
            return False

    def login(self,password):
        if password!= self.password:
            return False
        else:
            return True

if __name__ == "__main__":
    usuario=Usuario("pablo","phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))
           