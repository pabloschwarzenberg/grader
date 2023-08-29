class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        siffra=0
        bokstav=0
        criteria_l=0
        criteria=0
        for i in password:
            if i.isdigit():
                siffra+=1
                break
        for i in password:
            if i.isalpha():
                bokstav+=1
                break
        if len(password)>=8 and len(password)<=16:
            criteria_l+=2
        for i in password:
            if i.isalnum():
                pass
            else:
                criteria+=1
                break
        for i in password:
            if i.isupper():
                criteria+=1
                break
        if (siffra+bokstav+criteria_l)==4 and criteria>=1:
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