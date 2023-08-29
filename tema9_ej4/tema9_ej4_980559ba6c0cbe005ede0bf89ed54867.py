class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        def password_check(passwd): 
      
        SpecialSym =['$', '@', '#', '%'] 
        val = True
      
        if len(passwd) < 6: 
            print('length should be at least 6') 
            val = False
          
        if len(passwd) > 20: 
            print('length should be not be greater than 8') 
            val = False
          
        if not any(char.isdigit() for char in passwd): 
            print('Password should have at least one numeral') 
            val = False
          
        if not any(char.isupper() for char in passwd): 
            print('Password should have at least one uppercase letter') 
            val = False
          
        if not any(char.islower() for char in passwd): 
            print('Password should have at least one lowercase letter') 
            val = False
            
        if not any(char in SpecialSym for char in passwd): 
            print('Password should have at least one of the symbols $@#') 
            val = False
        if val: 
            return val 

    def login(self,password):
        pass

if __name__ == "__main__":
    usuario=Usuario("pablo","phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))
           