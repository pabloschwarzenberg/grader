class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""
        
    def __str__(self):
         return "Usuario({self.nombre},{self.email},{self.password})"
        
    #def validar_password(self,password)

    def cambiar_password(self,password):
        letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u",
          "v", "w", "x", "y", "z"]
        letrasmay = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U",
          "V", "W", "X", "Y", "Z"]
        numeros = ["1","2","3","4","5","6","7","8","9","0"]
        especiales = ["!","#","@","$","%","&","/","(",")","=","?","¡","'","¿","+","´","}","{","_"]
        a=0
        if len(password)<=16 and len(password)>=8:
            for index in password:
                if index in letras:
                    a+=1
  
            if a>0:
                a=0
                for index in password:
                    if index in letrasmay or index in especiales:
                        a+=1
                if a>0:
                    a=0
                    for index in password:
                        if index in numeros:
                            a+=1
                    
                    
                    
        if a>0:
            self.password = password
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
    
# NO ENTIENDO PORQUE DICE QUE clavesecreta1_ es TRUE si no tiene mayuscula          