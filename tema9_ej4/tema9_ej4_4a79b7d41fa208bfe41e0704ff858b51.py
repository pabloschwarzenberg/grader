from string import ascii_letters
from string import ascii_uppercase
from string import digits
from string import punctuation

class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        
        # convertir password en una lista llamada clave para comparar caracter a caracter
        clave = list(password)
        
        flag_letras = 0
        flag_numeros = 0
        flag_mayusculaocaracterespecial = 0 

        if 8<=len(clave)<=16:
            for i in range(len(clave)):
                
                if clave[i] in ascii_letters:                 
                    flag_letras = 1
                
                if clave[i] in digits:
                    flag_numeros = 1
                    
                if (clave[i] in ascii_uppercase) or (clave[i] in punctuation):
                    flag_mayusculaocaracterespecial = 1
            
            if flag_letras != 0 and flag_numeros != 0 and flag_mayusculaocaracterespecial != 0:
                self.password = "".join(clave)
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
    
    
    usuario= Usuario("pablo","phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clavesecreta1!"))
