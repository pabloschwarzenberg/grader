class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        if 8 <= len(password) <= 16:
            may = 0
            for i in range(65, 91):
                if chr(i) in password:
                    may += 1
            sm = 0
            for i in range(97, 123):
                if chr(i) in password:
                    sm += 1
            num = 0
            for i in range(48,58):
                if chr(i) in password:
                    num +=1
            rango = list(range(32,48)) + list(range(58,65)) + list(range(91,97))
            sp = 0
            for i in rango:
                if chr(i) in password:
                    sp += 1
            
            if  sm >= 1 and num >= 1 and (sp >= 1 or may >= 1):
                self.password = password
                return True
            else:
                return False
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
