class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""
    def clave_valida(self, password):
        if len(password)>=8 and len(password)<=16:
            contador_faltas=0
            if password==password.lower():
                contador_faltas+=1
                
            password=password.lower()
            letras="abcdefghijklmnopqrstuvwxyz"
            numeros="0123456789"
            
            litsta_letras=list(letras)
  
            litsta_numeros=list(numeros)
            contador_letras=0
            contador_numeros=0
            password1=password
            for i in password1:
                if i in litsta_letras:
                    password1=password1.replace(i,"")
                    contador_letras+=1
                if i in litsta_numeros:
                    password1=password1.replace(i,"")
                    contador_numeros+=1
            
            if len(password1)>0 and contador_letras>0 and contador_numeros>0:

                return True
            elif contador_letras>0 and contador_numeros>0 and contador_faltas==0:
                return True
            else:
                contador_faltas+=1
                if contador_faltas==2:

                    return False
        else:

            return False

    def cambiar_password(self, password):
        if Usuario(self.nombre,self.email).clave_valida(password)==True:
            self.password=password
            return True
        else:

            return False 
        
        pass

    def login(self,password):
        if self.password==password:
            return True
        else:
            return False
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
