class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        self.password = password
        if len(self.password)<8 or len(self.password)>16:
           return False
        else:
             clave = self.password
             if not ("1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9") in clave:
                   return False
             caracter_especial = 0
             mayusculas = 0
             for c in clave:
                if c=="a" or c=="b" or c=="c" or c=="d" or c=="e" or c=="f" or c=="g" or c=="h" or c=="i" or c=="j" or c=="k" or c=="l" or c=="m" or c=="n" or c=="o" or c=="p" or c=="q" or c=="r" or c=="s" or c=="t" or c=="u" or c=="v" or c=="w" or c=="x" or c=="y" or c=="z" or c=="0" or c=="1" or c=="2" or c=="3" or c=="4" or c=="5" or c=="6" or c=="7" or c=="8" or c=="9":
                     caracter_especial = 0
                else:
                     caracter_especial+=1
             for l in clave:
                 if l=="A" or l=="B" or l=="C" or l=="D" or l=="E" or l=="F" or l=="G" or l=="H" or l=="I" or l=="J" or l=="K" or l=="L" or l=="M" or l=="N" or l=="O" or l=="P" or l=="Q" or l=="R" or l=="S" or l=="T" or l=="U" or l=="V" or l=="W" or l=="X" or l=="Y" or l=="Z":
                     mayusculas+=1
             if caracter_especial == 0 and mayusculas == 0:
                  return False
             else:
                  self.password = password
                  return True
                  
                
      
                    

    def login(self,password):
        if self.password == password:
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
    
           



if __name__ == "__main__":
    usuario=Usuario("pablo","phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))
    
           
