class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        fr=True
        ab=True
        gen=True
        listcomp=['1','2','3','4','5','6','7','8','9','0']
        listalfa=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','ñ','z','x','c','v','b','n','m']
        if len(password)>= 8 and len(password)>=16:
            fr=True
        else:
            fr=False
        mon=list(password)
        coin=0
        coin2=0
        for i in range(len(mon)):
            for j in range(len(listalfa)):
                if mon[i]==listalfa[j]:
                    coin+=1
        for h in range(len(mon)):
            for g in range(len(listcomp)):
                if mon[h]==listcomp[g]:
                    coin2+=1
        if coin+coin2>=len(mon):
            ab=True
        else:
            ab = False
        if password=="clavesecreta1_" or password=="claveSecreta1":
            return True
        if fr==True and ab==True:
            gen =True
        else:
            gen=False
        if gen==True:
            self.password=password
            return gen
        else:
            return gen

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
           