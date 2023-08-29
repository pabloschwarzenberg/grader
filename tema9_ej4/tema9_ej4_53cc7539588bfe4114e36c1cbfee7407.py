class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        password_l=list(password)
        if 8<=len(password_l)<=16:
            n=1
            while n==1:
                for m in range(len(password_l)):
                    if password_l[m].isdigit()==True:
                        n=2
                        break
                    else:
                        continue
                if n==2:
                    continue
                else:
                    return False
            while n==2:
                for b in range(len(password_l)):
                    if password_l[b].isalpha()==True:
                        n=3
                        break
                    else:
                        continue
                if n==3:
                    continue
                else:
                    return False
                return False
            while n==3:
                print("pase de nuevo")
                listado={"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","T","U","V","W","X","Y","Z","!","·","$","%","&","/","(",")","=","?","¿","_","-","¨"}
                for v in range(len(password_l)):
                    if password_l[v] in listado:
                        n=4
                    else:
                        continue
                if n==4:
                    self.password=password
                    return True
                else:
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
           