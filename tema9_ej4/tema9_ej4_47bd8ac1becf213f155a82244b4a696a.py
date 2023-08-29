class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        numeros=[]
        especiales=[]
        if 8<=len(password)<=16:
            for i in password:
                if 33<=ord(i)<=47 or 58<=ord(i)<=96 or 123<=ord(i)<=126:
                    especiales.append(i)
            for i in password:
                if 48<=ord(i)<=57:
                    numeros.append(i)
                
            if len(especiales)>=1 and len(numeros)>=1:
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