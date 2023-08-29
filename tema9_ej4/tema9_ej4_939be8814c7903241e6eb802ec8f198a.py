class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):

        Chars = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

        lchars=[]
        for x in Chars:
            lchars.append(x)
        lnumeros =[]    
        Numeros="12345678900"
        for x in Numeros:
            lnumeros.append(x)
        CMayus = 0
        Symbs = "='\]:;-[!@#$%^&*()_+´<>/?-,{}¿"
        CSymbs=0
        lsymbolos=[]
        for x in Symbs:
            lsymbolos.append(x)
        numeritos=0
        Cminus= 0
        if len(password)>=8 and len(password)<=16:

            for x in password:
                aux = x.upper()
                if aux in lchars:
                    if x in lchars:
                        CMayus+=1
                    else:
                        Cminus+=1
                
                
                if x in lsymbolos:
                    CSymbs+=1
                if x in lnumeros:
                    numeritos = numeritos +1
                
                    
            
##           for x in password:
##               
##           for x in password:
##               
            if CMayus>=1 and numeritos>=1 and Cminus>=1:
                
                self.password = password
                return True
            elif  CSymbs>= 1 and numeritos>=1 and Cminus>=1:
                
                self.password = password
                return True
            else:
                return False
                print("deberia estar aca")
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