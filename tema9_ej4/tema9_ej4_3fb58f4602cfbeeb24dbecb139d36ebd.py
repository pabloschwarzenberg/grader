class Usuario:
    def __init__(self,nombre,email,):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        especial=False
        mayus=False
        num=False
        let=False
        letras=["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
        mayusculas=["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]
        caracteres_especiales=["#","!","$","*","_"]
        numeros=["0","1","2","3","4","5","6","7","8","9"]
        if len(password)>=8 and len(password)<=16:
            for i in password:
                if i in caracteres_especiales:
                    especial=True
                elif i in mayusculas:
                    mayus=True
                elif i in numeros:
                    num=True
                else:
                    let=True
            if (let and num) and (mayus or especial):
                self.password=password
                return True
            else:
                return False
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
           