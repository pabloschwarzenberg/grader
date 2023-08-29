class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        abc="abcdefghijklmnopqrstuvwxyz"
        ABC="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        simbolos="!#$%&=_-.?¡¿*´[]"
        numeros="1234567890"
        vf=[]
        lABC=[]
        labc=[]
        lnumeros=[]
        lsimbolos=[]
        
        if 8<=len(password)<=16:
            vf.append(True)
        for i in password:
            if (i in ABC):
               lABC.append(i)
            if (i in numeros):
                lnumeros.append(i)
            if (i in abc):
                labc.append(i)
            if (i in simbolos):
                lsimbolos.append(i)
                
        print(labc,lABC,lnumeros,lsimbolos)  
        if (len(labc)!=0) and (len(lnumeros)!=0):
            vf.append(True)
        if (len(lABC)!=0) or (len(lsimbolos)!=0):
            vf.append(True)

        if vf.count(True)==3:
            self.password=password
            return True
        
        else:
            return False
        ##Debe tener minimo 8 caracteres max 16-contiene letras y numeros
        #contiene al menos una mayuscula o caracter especial (simbolo)
        #si cumple con esto, retornar True


    def login(self,password):
        if password==self.password:
            return True
        else:
            return False            
        #retorna true si la password ingresasa corresponde


if __name__ == "__main__":
    usuario=Usuario("pablo","phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))