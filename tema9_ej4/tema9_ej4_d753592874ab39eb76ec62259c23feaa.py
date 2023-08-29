class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        alfabeto=["a","b","c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m","n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        ALFABETO=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numeros=["1","2","3","4","5","6","7","8","9","0"]
        caracter_especial=["!","'","#","$","%","&",",",".",";","_","-","/","(",")","=","?","¡","¿","@",'"']
        lista=[]
        
        if len(password)>7 and len(password)<17:
            contador=0
            for caracter in password:
                if caracter in alfabeto:
                    contador+=1
                    if contador==1:
                        break
            for caracter in password:
                if caracter in numeros:
                    contador+=1
                    if contador==2:
                        break
            for caracter2 in password:
                if caracter2 in ALFABETO or caracter2 in caracter_especial:
                    contador+=1
            print(contador)
            if contador>=3:
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
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))