class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        j=0
        for i in password:
            j+=1
        if j>=8 and j<=16:
            lista=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
            num=["1","2","3","4","5","6","7","8","9","0"]
            mayusculas=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
            s=0
            nums=0
            mayu=0
            otro=0
            for i in password:
                if i in lista:
                    s+=1
                elif i in num:
                    nums+=1
                elif i in mayusculas:
                    mayu+=1
                else:
                    otro+=1
            if s>0 and nums>0:
                if mayu>0 or otro>0:
                    self.password=password
                    return True
                else:
                    return False
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
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))
           