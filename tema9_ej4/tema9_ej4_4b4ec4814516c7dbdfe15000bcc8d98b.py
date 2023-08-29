class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.clave=''
    def cambiar_password(self,password):
        self.password=[]
        for i in password:
            self.password.append(i)
       
        if len(self.password)<=16 and len(self.password)>=8:
            a=0
            b=0
            c=0
            for caracter in self.password:
                if ord(caracter) in range(97,122): #letras
                    a=1
                elif ord(caracter) in range(48,57): #numeros
                    b=1
                elif (ord(caracter) in range(33,47)) or (ord(caracter) in range(91,96)) or (ord(caracter) in range(65,90)): #simbolos,mayusculas
                    c=1
            if a==1 and b==1 and c==1:
                self.clave=password
                return True
            else:
                return False
        else:
            return False
                
    def login(self,password):
        if password==self.clave:
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
           