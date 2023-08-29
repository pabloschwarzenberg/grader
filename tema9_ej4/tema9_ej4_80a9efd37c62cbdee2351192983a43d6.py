class Usuario:
    def __init__(self,nombre,email):
        self.nombre = nombre
        self.email = email
        self.password =""

    def cambiar_password(self,password):
        if len(password)>= 8 and len(password)<=16 :
            pas =[]
            pas_ascii= []
            for i in password:
                pas.append(i)
            print(pas)
            for i in pas:
                ascii= ord(i)
                pas_ascii.append(ascii)
            print(pas_ascii)
            for i in pas_ascii:
                n = 0
                while n < len(pas_ascii):
                    if (pas_ascii[n] >= 48 and pas_ascii[n]<= 57) or (pas_ascii[n]>=97 and pas_ascii[n]<= 122 ):
                        for i in pas_ascii:
                            b = 0
                            while b < len(pas_ascii):
                                if (pas_ascii[b]>=65 and pas_ascii[b]<=90 )or (pas_ascii[b]>= 91 and pas_ascii[b]<= 96):
                                    self.password = password
                                    return True
                                b+=1
                            else:
                                return False
                    n+=1
                else:
                    return False
        else:
            return False

    def login(self,password):
        if self.password == password:
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
           