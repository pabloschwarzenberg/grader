class Usuario:
    
    def __init__ (self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=''
    def cambiar_password(self,password):
        rara=0
        letras=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        numeros=['1','2','3','4','5','6','7','8','9','0']
        LETRASRARAS=['#','$','%','&','/','(',')','=',"'",'?','¿','+','*','¡','!','_']
        for i in letras:
            LETRASRARAS.append(i.upper())
        if not(8<=len(password)<=16):
            return False
        for i in password:
            if (i in letras) or (i in LETRASRARAS)or (i in numeros):
                if i in LETRASRARAS:
                    rara+=1
            else:
                return False
        if rara==0:
            return False
        else:
            self.password=password
            return True
        
    def login (self,password):
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
           