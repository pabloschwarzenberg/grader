class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        j=0
        a=0
        signos=["*","#","_","-","!","?","$"]
        ABC=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","X","Z"]
        if 8<=len(password)<=16:
            self.password=""
            for numero in range(0,10):
                if str(numero) in password:
                    j=j+1
            if j!=0:
                for letra in password:
                    if (letra in signos) or (letra in ABC):
                        a=a+1
                if a!=0:
                    self.password=self.password+password
                    return True
                else:
                    return False
            else:
                return False
                     
        else:
            return False

    def __str__(self):
        return self.password

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
          