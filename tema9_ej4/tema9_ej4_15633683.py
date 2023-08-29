class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=''
    def __str__(self):
        return '{0},{1},{2}'.format(self.nombre,self.email,self.password)
    def cambiar_password(self,password):
        lista_letras=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
        lista_numeros=['1','2','3','4','5','6','7','8','9','0']
        lista_especiales=['_','-','!','@','#','$','%','&','*','+']
        letras=0
        numeros=0
        mayusculas=0
        especial=0
        for i in lista_letras:
            if password.find(i)!=-1:
                letras+=1
        for i in lista_numeros:
            if password.find(i)!=-1:
                numeros+=1
                mayusculas-=1
        for i in lista_especiales:
            if password.find(i)!=-1:
                especial+=1
                mayusculas-=1
        for i in password:
            if i.upper()==i:
                mayusculas+=1
        print(letras)
        print(numeros)
        print(mayusculas)
        print(especial)
                
            
        if 7<len(password)<17 and numeros>0 and letras>0 and (mayusculas>0 or especial>0):
            self.password=password
            return True
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