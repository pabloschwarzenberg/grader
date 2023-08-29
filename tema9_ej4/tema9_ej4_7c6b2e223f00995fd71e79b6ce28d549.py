class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        validador=False
        if len(password)>=8 and len(password)<=16:
                    
            for letra in password:
                
                if letra=='a' or letra=='b' or letra=='c' or letra=='d' or letra=='e' or letra=='f' or letra=='g' or letra=='h' or letra=='i' or letra=='j' or letra=='k' or letra=='l' or letra=='m' or letra=='n' or letra=='ñ' or letra=='o' or letra=='p' or letra=='q' or letra=='r' or letra=='s' or letra=='t' or letra=='u' or letra=='v' or letra=='w' or letra=='x' or letra=='y' or letra=='z':
                    
                    for numero in password:
                        
                        if numero=='0' or numero=='1' or numero=='2' or numero=='3' or numero=='4' or numero=='5' or numero=='6' or numero=='7' or numero=='8' or numero=='9':
                            
                            for caracter in password:
                                
                                if caracter=='!' or caracter=='_' or caracter=='-' or caracter=='.' or caracter==':' or caracter==',' or caracter==';' or caracter=='#' or caracter=='$' or caracter=='%' or caracter=='&' or caracter=='A' or caracter=='B' or caracter=='C' or caracter=='D' or caracter=='E' or caracter=='F' or caracter=='G' or caracter=='H' or caracter=='I' or caracter=='J' or caracter=='K' or caracter=='L' or caracter=='M' or caracter=='N' or caracter=='Ñ' or caracter=='O' or caracter=='P' or caracter=='Q' or caracter=='R' or caracter=='S' or caracter=='T' or caracter=='U' or caracter=='V' or caracter=='W' or caracter=='X' or caracter=='Y' or caracter=='Z':
                                   
                                    self.password=password
                                    return True
        return validador                                        
            
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