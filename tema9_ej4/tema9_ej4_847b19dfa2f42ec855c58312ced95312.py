class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        if 8<=len(password)<=16:
            for i in range(0,len(password)):
                letra=password[i]
                if letra.isnumeric()==True:
                    lista=["#","$","%","&","_"]
                    for j in range (0,len(password)):
                        letra=password[j]
                        if letra.isupper():
                            password="".join(password)
                            self.password=password
                            return True
                    for elemento in lista:
                        if elemento in password:
                            password="".join(password)
                            self.password=password
                            return True
                        
                    return False
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
           