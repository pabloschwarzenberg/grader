class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        letras=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        numeros=["1","2","3","4","5","6","7","8","9"]
        letrasm=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        a=0
        b=0
        c=0
        d=0
        if 8<=len(password)<=16:
            for i in password:
                if i in letras:
                    a=a+1
                elif i in numeros:
                    b=b+1
                elif i in letrasm:
                    c=c+1
                else:
                    d=d+1
            if a>=1 and b>=1 and (c>=1 or d>=1):
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
