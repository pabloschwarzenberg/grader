class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        b=list(password)
        num=["1","2","3","4","5","6","7","8","9","0"]
        abc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        for i in num:
            while i in b:
                b.remove(i)
        for u in abc:
            while u in b:
                b.remove(u)
        while(" ") in b:
            b.remove(" ")
        b="".join(b)
        if 8<=len(password)<=16:
            if "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "0" in password:
                if password.lower()!=password or len(b)!=0:
                    self.password=password
                    return True
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
           