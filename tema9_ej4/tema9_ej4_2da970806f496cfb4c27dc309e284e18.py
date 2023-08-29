class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        a=False
        numeros=[]
        letras=[]
        mayusculas=[]
        dist=[]
        abecedario="abcdefghijklmnñopqrstvwxyz0123456789"
        if 8<=len(password)<=16:
            for i in password:
                if i in abecedario[25:]:
                    numeros.append(i)
            if len(numeros)!=0:
                for i in password:
                    i.lower()
                    if i in abecedario[0:25]:
                        letras.append(i)
                if len(letras)!=0:
                    for i in letras:
                        if i==i.upper():
                            mayusculas.append(i)
                    if len(mayusculas)!=0:
                        self.password=password
                        a=True
                    for i in password:
                        if i not in abecedario:
                            dist.append(i)
                        if len(dist)!=0:
                            self.password=password
                            a=True
        return a
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
           