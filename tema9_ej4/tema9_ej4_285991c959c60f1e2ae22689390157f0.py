class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        if 8 <=len(password)<=16:
            numeros=["0","1","2","3","4","5","6","7","8","9"]
            
            num=False
            for i in numeros:
                if i in password:
                    num=True
                    
            esp=False
            for j in password:
                if not j.isalpha() and  j.isdigit():
                    esp=True
                    
            mayuscula=False
            for k in password:
                if (k == k.upper() and k.isalpha()) or (not  k.isalnum()):
                    mayuscula=True

            if num and esp and mayuscula:
                self.password=password
                return True                
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
