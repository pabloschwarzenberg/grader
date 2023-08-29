class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        if self.password != password:
            if ((len(password) >= 8) and (len(password) <= 16)):
                for i in password:
                    if i.isalpha():
                        a=[""]
                        for j in password:
                            if not j.isalpha():
                                a=["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Ñ","Z","X","C","V","B","N","M"]
                                b=["1","2","3","4","5","6","7","8","9","0"]
                                for z in password:
                                    if z in a or (not z.isalpha() and z not in b):
                                        self.password=password
                                        return True
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
