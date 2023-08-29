class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        contador=0
        for i in password:
            contador+=1
        if contador>16 or contador<8:
            return False
        else:
            letras=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
            letrasmayus=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
            numeros=["0","1","2","3","4","5","6","7","8","9"]
            cosas=["_"]
            letras2=[]
            numeros2=[]
            cosas2=[]
            letras3=[]
            for i in password:
                if (i in letras)==True:
                    letras2.append(i)
                if (i in numeros)==True:
                    numeros2.append(i)
                if (i in cosas)==True:
                    cosas2.append(i)
                if (i in letrasmayus)==True:
                    letras3.append(i)
            if (letras2!=[]) and (numeros2!=[]) and ((cosas2!=[]) or (letras3!=[])):
                return True
                self.password=password
            else:
                return False

    def login(self,password):
        if password==self.password:
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