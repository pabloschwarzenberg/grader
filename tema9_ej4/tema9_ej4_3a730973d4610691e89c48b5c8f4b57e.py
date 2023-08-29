class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        i=0
        letras=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        numeros=["1","2","3","4","5","6","7","8","9","0"]
        
        largo=False
        if len(password)>7 or len(password)<17:
          largo=True
        
        mayusculas=False        
        for m in range(len(password)-1):
           if password[m] in letras:
                mayusculas=True
     
        caracter=False
        if password.isalnum()==False:
              caracter=True
         
        numero=False 
        for n in range(len(password)):
          if password[n] in numeros:
                 numero=True  
               
           
        if largo==True and numero==True and caracter==True:
           self.password=password
           return True
              
        if largo==True and numero==True and mayusculas==True:
           self.password=password
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
           