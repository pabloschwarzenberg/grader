        
class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
    #entre 8 y 16 caracteres, letras y numeros, una mayuscula y un caracter especial
        numero=['1','2','3','4','5','6','7','8','9','0']
        abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        ABC = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        caracter=0
        mayuscula=0
        n=0
        simbolo=0
        for i in password:
            if i in abc:
               caracter=1
            elif i in ABC:
                mayuscula=1
            elif i in numero:
                n=1
            else:
                simbolo=1
        if 8<=len(password)<=16 and caracter==1  and n==1 and (simbolo==1 or  mayuscula==1):
            self.password=password
            return True
        else:
            return False
        pass

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
    

           