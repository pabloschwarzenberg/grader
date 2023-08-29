class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.clave=None
    def cambiar_password(self,clave):
        self.clave=clave
        letras=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        numeros=["0","1","2","3","4","5","6","7","8","9"]
        if len(self.clave)>7 and len(self.clave)<17:
            requisitos=[]
            for x in self.clave:
                if x in letras:
                    requisitos.append("Letra")
                elif x in numeros:
                    requisitos.append("Numero")
                else:
                    requisitos.append("Especial")
            if "Letra" in requisitos:
                if "Numero" in requisitos:
                    if "Especial" in requisitos:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
                
        else:
            return False
    def login(self,password):
        if password==self.clave:
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
           