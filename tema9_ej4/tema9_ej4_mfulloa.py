class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        #chequeo mayusculas
        cont=0
        for x in password:
            for y in range(65,91):
                if chr(y)==x:
                    cont+=1
        cont2=0
        for x in password:
            for y in range(48,58):
                if chr(y)==x:
                    cont2+=1
        cont3=0
        for x in password:
            for y in range(97,123):
                if chr(y)==x:
                    cont3+=1
        if cont2==0:
            return False
        if cont3==0:
            return False
        if cont==0 and cont2+cont3==len(password):
            return False
        if len(password)>=8 and len(password)<=16:
            self.password=password
            return True
        return False

    def login(self,password):
        if password==self.password:
            return True
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