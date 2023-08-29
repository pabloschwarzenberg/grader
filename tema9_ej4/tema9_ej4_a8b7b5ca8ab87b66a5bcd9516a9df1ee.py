class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        largo=0
        mayus_caract=0
        letras=0
        numeros=0
        
        
        if len(password)<16 and len(password)>8:
            largo+=1
        for i in password:
            
            if i.isalpha() == True:
                letras+=1
                
                if i.isupper() ==True:
                    mayus_caract+=1
            else:
                if i.isdigit()==True:
                    
                    numeros +=1
                else:
                    
                    mayus_caract +=1
        
        if largo>0 and letras >0 and mayus_caract>0 and numeros >0:
            self.password=password
            return True
        else:
            return False

        

    def login(self,password):
        if password == self.password:
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
           
           