class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=''

    def cambiar_password(self,password):
        s=[]
        n=[]
        w=[]
        m=[]
        abcd='qwertyuiopasdfghjklñzxcvbnm'
        for i in password:
            try:
                int(i)
                n.append(i)
            except ValueError:
                if abcd.find(i)!=-1:
                    s.append(i)
                elif abcd.upper().find(i)!=-1:
                    m.append(i)
                else:
                    w.append(i)
        if len(s)>0 and len(n)>0 and len(s)<len(password) and len(w)<len(password) and len(n)<len(password) and len(password)>=8 and len(password)<=16:
            if len(w)>0 or len(m)>0:
                self.password=password
                return True
            else:
                return False
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
    print(usuario.cambiar_password("clavesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))
           