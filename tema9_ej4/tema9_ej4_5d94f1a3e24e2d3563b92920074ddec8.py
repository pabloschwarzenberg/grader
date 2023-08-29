class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        l="abcdefghijklmnopqrstuvwxyz"
        n="0123456789"
        s="#@*&%$!+_"
        m="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        cl=0
        cn=0
        cs=0
        cm=0
        if 8<=len(password)<=16:
            for i in l:
                if password.find(i)!=-1:
                    cl+=1
            for j in n:
                if password.find(j)!=-1:
                    cn+=1
            for k in s:
                if password.find(k)!=-1:
                    cs+=1
            for z in m:
                if password.find(z)!=-1:
                    cm+=1
                                           
            if cl>0 and cn>0 and (cs>0 or cm>0):
                self.password=password
                return True

            else:
                return False 
        else:
            return False
        pass

    def login(self,password):
        if password==self.password:
            return True
        else:
            return False
        pass

if __name__ == "__main__":
    usuario=Usuario("pablo","phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))