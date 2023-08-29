class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        if 7<len(password)<17:
            p=list(password)
            a=[]
            for caracter in p:
                caracter=ord(caracter)
                a.append(caracter)
            l=0
            n=0
            M=0
            s=0
            for numero in a:
                if 32<numero<48:
                    s=s+1
                elif 47<numero<58:
                    n=n+1
                elif 57<numero<65:
                    s=s+1
                elif 64<numero<91:
                    M=M+1
                elif 90<numero<97:
                    s=s+1
                elif 96<numero<123:
                    l=l+1
                elif 122<numero<256:
                    s=s+1
            if l!=0 and n!=0 and (M!=0 or s!=0):
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
           