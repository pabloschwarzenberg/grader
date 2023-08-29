class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        if 8<=len(password)<=16:
            num=[0,1,2,3,4,5,6,7,8,9]
            abecedario=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
            sig=[")","_","=","?","¿","*","+","#"]
            mayusculas=0
            numeros=0
            signos=0
            for i in password:
                for j in num:
                    j=str(j)
                    if i==j:
                        numeros+=1
                for k in abecedario:
                    if i==k:
                        mayusculas+=1
                for l in sig:
                    if i==l:
                        signos+=1
            if (mayusculas>0 or signos>0) and numeros>0:
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
    print(usuario.cambiar_password("clavesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))
           