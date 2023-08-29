class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        passwordm=password
        passwordm=passwordm.lower()
        if (len(password)>=8 and len(password)<=16): 
            for i in password:
                if ((ord(str(i))>=91 and ord(str(i))<=96) or (ord(str(i))>=58 and ord(str(i))<=64) or (ord(str(i))>=123 and ord(str(i))<=126) or (ord(str(i))>=33 and ord(str(i))<=47)) or passwordm!=password:
                    for i in password:
                        if ord(str(i))>=48 and ord(str(i))<=57:
                            self.password=password
                            return True
        return False

    def login(self,password):
        passwordv=password
        if self.password==passwordv:
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
           