class Usuario:                                             
    def __init__(self, nombre, email):                     
        self.nombre = nombre                               
        self.email = email                                 
        self.password = ""                                 
                                                           
                                                           
    def cambiar_password(self, new_password):              
      abc=list('abcdefghijklmnopqrstuvwxyz1234567890')     
      cara=list('<>_-:.;,?¿¡=+*ç¨$%&/()!@')                
      new_password=new_password                            
      if 8<=len(new_password) and len(new_password)<=16:   
       letras=False                                        
       numeros=False                                       
       mayusculas=False                                    
       caracteres=False                                    
       cara = list('<>_-:.;,?¿¡=+*ç¨$%&/()!@')             
       for variable in new_password:                       
           if variable.isdigit()==True:                    
               numeros=True                                
           if variable.isalpha()==True:                    
               letras=True                                 
           if variable.isupper()==True:                    
               mayusculas=True                             
           if variable in cara:                            
               cara=True                                   
       if numeros is True:                                 
           if letras is True:                              
               if (mayusculas or cara) is True:            
                   self.password=new_password              
                   return True                             
               else:                                       
                   return False                            
           else:                                           
               return False                                
       else:                                               
           return False                                    
      else:                                                
          return False                                     
                                                           
    def login(self, password):                             
        if self.password==password:                        
            return True                                    
        else:                                              
            return False                                   
                                                           
                                                           
if __name__ == "__main__":                                 
    usuario = Usuario("pablo", "phschwarzenberg@uc.cl")    
    print(usuario.cambiar_password("clave"))               
    print(usuario.cambiar_password("clavesecreta1_"))      
    print(usuario.cambiar_password("clavesecreta"))        
    print(usuario.cambiar_password("clasesecreta1"))       
    print(usuario.cambiar_password("claveSecreta1"))       
    print(usuario.login("clavesecreta1_"))                 
    print(usuario.login("claveSecreta1"))                  