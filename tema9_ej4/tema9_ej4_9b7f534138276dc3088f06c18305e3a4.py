class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        l_password=list(password)
        numeros=["1","2","3","4","5","6","7","8","9"]
        a=False
        b=False
        c=False
        d=False
        letras=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
        caracter_especial=["#","*","!","+","-","%","_","-","?","¿","¡",">","<","=","[","]","{","}","$","&","/","(",")","'",'"',";","|","°","¬","^","`",":","@"]
        if len(l_password)>8 and len(l_password)<16:
            for i in l_password:
                for j in numeros:
                    if i==j:
                        a=True
                for j in letras:
                    if i==j:
                        b=True
                for j in letras:
                    if j.upper()==i:
                        c=True
                for j in caracter_especial:
                    if i==j:
                        d=True
            if a==True and b==True and (c==True or d==True):
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
    print(usuario.login("claveSecreta1"))
           