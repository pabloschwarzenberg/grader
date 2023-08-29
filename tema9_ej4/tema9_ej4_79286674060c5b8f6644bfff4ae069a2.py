class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        numeros="0123456789"
        letras="abcdefghijklmnñopqrstuvwxyz"
        letras=[i for i in letras]
        letras_mayus=[i.upper for i in letras]
        numeros=[i for i in numeros]
        if 8<=len(password)<=16:
            check_letras=0
            for c in password:
                if c in letras:
                    check_letras=1
                    break
                else:
                    pass

            check_mayus=0
            for c in password:
                if c in letras_mayus or (c not in letras_mayus and c not in letras and c not in numeros):
                    check_mayus = 1
                    break
                else:
                    pass

            check_num=0
            for c in password:
                if c in numeros:
                    check_num = 1
                    break
                else:
                    pass
            if check_letras==1 and check_mayus==1 and check_num==1:
                self.password=password
                return True
            else:
                return False
        else:
            return False


    def login(self, password):
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
           