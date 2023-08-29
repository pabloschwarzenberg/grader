class Usuario:

    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        if 8<=len(password) and len(password)<=16:
                                    abc="abcdefghijklmnñopqrstuvwxyz"
                                    num="0123456789"
                                    v=False
                                    w=False
                                    b=False
                                    x=False
                                    for letra in abc:
                                        if letra in password:
                                            v=True
                                    abcd=abc.upper()
                                    for letra in abcd:
                                        if letra in password:
                                            x=True
                                    for numero in num:
                                        if numero in password:
                                            b=True
                                    clave=password
                                    for i in clave:
                                        if i in abc:
                                            clave=clave.replace(i,"")
                                        if i in num:
                                            clave=clave.replace(i,"")
                                        print(clave)
                                    if clave!="":
                                        w=True
                                    if v==True and b==True and (x==True or w==True):
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
    print(usuario.cambiar_password("clasesecreta1"))####t
    print(usuario.cambiar_password("claveSecreta1"))#t
    print(usuario.login("clavesecreta1_"))#f
    print(usuario.login("claveSecreta1")) #t 