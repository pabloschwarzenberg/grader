class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        if len(password)>=8 and len(password)<=16:
            abecedario=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
            numeros=["0","1","2","3","4","5","6","7","8","9"]
            hayletra=False
            haynumero=False
            hayce=False
            for i in password:
                if (i in abecedario):
                    hayletra=True
                    break
            for i in password:
                if (i in numeros):
                    haynumero=True
                    break
            for i in password:
                if not(i in abecedario) and not(i in numeros) and i!=" ":
                    hayce=True
                    break
            if hayletra and haynumero and hayce:
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
           