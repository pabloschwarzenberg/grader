class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""
    def cambiar_password(self,password):
        if 8<=len(password)<=16:
            j=0
            while j<10:
                a=password.find(str(j))
                if a!=-1:
                    i=0
                    while i<len(password):
                        if ord(password[i])<48 or 57<ord(password[i])<97 or 122<ord(password[i]):
                            self.password=password
                            return True
                        else:
                            i=i+1
                    return False
                else:
                    j=j+1
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