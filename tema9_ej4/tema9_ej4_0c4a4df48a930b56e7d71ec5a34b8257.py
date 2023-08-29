class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        numeros = [1,2,3,4,5,6,7,8,9,0]
        comparar=password.lower()
        comparar2=password.upper()
        if len(password) in range (8,17):
            if password != comparar and password != comparar2 :
                i=str(1)
                if password.find(i) != -1:   
                    clave= password
                    print(clave)
                    return True
            if True:
                if password.find("_") != -1 :
                        return True
                        i=str(1)
                        if password.find(i) != -1:   
                            clave= password
                            print(clave)
                            return True
                else:
                        return False
                
            else: 
                return False
        else:
            return False
                
            
        pass

    def login(self,password):
        if password != self.password:
            return False
        else:
           return True
        pass

if __name__ == "__main__":
    usuario=Usuario("pablo","phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))

