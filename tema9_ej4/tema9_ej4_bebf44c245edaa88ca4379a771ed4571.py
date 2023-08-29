class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        if len(password)<=16 and len(password)>=8:
            alfaMay=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
            clave=list(password)
            let=""
            num=""
            otr=""
            for letra in clave:
                if letra.isalpha()==True:
                    if letra in alfaMay:
                        otr+=letra
                    else:
                        let+=letra
                elif letra.isdigit()==True:
                    num+=letra
                else:
                    otr+=letra
            if len(let)>0 and len(num)>0 and len(otr)>0:
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
           