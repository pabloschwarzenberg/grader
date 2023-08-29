class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        simbolos=["_","#","$","%","&","/","=","¡","*","+","-","."]
        i=0
        k=0
        a=False
        b=False
        c=False
        d=False
        while i<len(simbolos):
            if simbolos[i] in password:
                a=True
                break
            i+=1
        if 8<=len(password)<=16:
            b=True
        while k<len(password):
             passwordd=list(password)
             if passwordd[k].isdigit()==True:
                 c=True
                 break
             k+=1
        if len([a for a in password if a.isupper()])>0:
            d=True
        if a==True or d==True:
            if b==True and c==True:
                self.password=password
                return True
                            
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
           