class Usuario:
    def __init__(self,nombre,email):
        self.password=''
        self.nombre=nombre
        self.email=email
    def cambiar_password(self,password):
        numero1=('1234567890')
        letras1=('qwertyuiopasdfghjklñzxcvbnm')
        simbolos1=('!#$%&/()=?¿¡*-+_')
        letras=0
        numeros=0
        simbolos=0
        mayusculas=0
        for i in password:
            if numero1.find(i)!=-1:
                numeros+=1
            if letras1.find(i)!=-1:
                letras+=1
            if simbolos1.find(i)!=-1:
                simbolos+=1
        for t in range (len(password)):
            if password[t].upper()==password[t]:
                    mayusculas+=1
        mayusculas=mayusculas-simbolos-numeros

        if 8<len(password)<16 and letras>0 and numeros>0 and (simbolos>0 or mayusculas>0):
            
            self.password=password
            return True
        else:
            return False
    def login(self,password):
        if self.password==password:
            return True
        else:
            self.password!=password
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

if __name__ == "__main__":
    usuario=Usuario("pablo","phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))
           