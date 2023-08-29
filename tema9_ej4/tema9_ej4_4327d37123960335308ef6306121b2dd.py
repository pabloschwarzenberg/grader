class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""
        
    def cambiar_password(self,password):
        self.password=password
        reglas_cumplidas=0
        contador=0
        ABC=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        mayusculas=0
        
        for simbolo in range(len(password)):
            if password[simbolo]=="_":
                contador+=1
            else:
                pass
            
        for letra in range(len(password)):
            if password[letra] in ABC:
                mayusculas+=1
            else:
                pass
                
        if contador>=1:
            reglas_cumplidas+=1
        if 8<=len(password)<=16:
            reglas_cumplidas+=1
        if mayusculas>0:
            reglas_cumplidas+=1

        if reglas_cumplidas>=2:
            return True
        else:
            return False
        

    def login(self,password):
        self.password=password
        if Usuario.cambiar_password(self,password) is True and Usuario.cambiar_password(self,password)==password:
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
        
