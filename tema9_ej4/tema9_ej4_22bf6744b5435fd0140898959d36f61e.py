class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        cuentaletras=0
        cuentanumeros=0
        cuentamayusculas=0
        abc="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
        for elemento in password:
            if elemento in abc:
                cuentamayusculas+=1
            elif elemento.isdigit()==True:
                cuentanumeros+=1
            elif elemento.isalpha()==True:
                cuentaletras+=1
            else:
                pass
                
        total=cuentaletras+cuentanumeros        
                
        if 7<len(password)<17 and cuentanumeros>0 and cuentaletras>0 and total<len(password):
            self.password+=password
            return True
            
        else:
            return False

    def login(self,password):
        if self.password==password:
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
           