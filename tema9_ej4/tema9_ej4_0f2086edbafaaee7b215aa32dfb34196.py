class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def __le__(self,other):
        if self.password <= other.password:
            return True
        else:
            return False

    def cambiar_password(self,password):
        list(password)
        cuenta=0
        for i in password:
            numero = ord(i)
            if 48 <= numero <= 57:
                cuenta = cuenta + 1
                
        cuenta2=0
        for l in password:
            numero2 = ord(l)
            if 65 <= numero2 <= 90:
                cuenta2 = cuenta2 + 1
        cuenta3= 0               
        for m in password:
            numero3 = ord(m)
            if 33 <= numero3 <= 47 or 58 <= numero3 <= 64 or 91 <= numero3 <= 96 or 123 <= numero3 <= 126:
                cuenta3 = cuenta3 + 1
        if 8<=len(password)<=16 and cuenta >= 1 and (cuenta2 >= 1 or cuenta3 >= 1):
            self.password = password 
            return True
        else:
            return False 
                 
                
    def __eq__(self,other):
        if self.password == other.password:
            return True
        else:
            return False
    def login(self,password):
        if self.password ==  password:
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