class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        if 8<=len(password)<=16:
            lista=[]
            for c in password:
                if 97<=ord(c)<=122 or 48<=ord(c)<=57:
                    lista.append('correct')
                elif 65<=ord(c)<=90:
                    lista.append('mayus')
                elif 33<=ord(c)<=47 or 58<=ord(c)<=64 or 91<=ord(c)<=96:
                    lista.append('chr')
            if len(lista)==len(password) and (('correct' in lista) and (('mayus' in lista) or ('chr' in lista))):
                self.password=password
                return True
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
           