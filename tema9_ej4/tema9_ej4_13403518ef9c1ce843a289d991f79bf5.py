class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        a=0
        nums="1234567890"
        letras="abcdefghijklmnopqrstuvwzxy"
        weas="!#$%&/()=?¡¿'|°<>-_{[´*.:;,_"
        b=0
        c=0
        d=0

        if len(password)>=8 and len(password)<=16:
            a+=1
        for i in nums:
            if i in password:
                b+=1
        if b>0:
            a+=1
        for i in letras:
            if i in password:
                c+=1
        if c>0:
            a+=1
        if password.lower() != password:
            a+=1
        else:
            for i in weas:
                if i in password:
                    d+=1
        if d>0:
            a+=1
                   
        if a ==4:
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
           

           