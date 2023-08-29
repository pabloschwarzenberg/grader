abc=list(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","s","r","t","u","v","x","y","z"])
Abc=list(["A","_","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","S","R","T","U","V","X","Y","Z"])
nume=list(["1","2","3","4","5","6","7","8","9","0"])
def condiciones(contra):
    a=0
    b=0
    c=0
    d=0
    e=0
    for i in contra:
        if (i in abc)==True:
            a=1
        elif (i in Abc)==True or i.isalnum==False:
            b=1
        elif (i in nume)==True:
            c=1
    if a!=0 and b!=0 and c!=0:
        return True
    elif a==0 or b==0 or c==0:
        return False
if __name__ == "__main__":
    print(condiciones("clave"))
    print(condiciones("clavesecreta1_"))
    print(condiciones("clavesecreta"))
    print(condiciones("clasesecreta1"))
    print(condiciones("claveSecreta1"))
class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
       if condiciones(password)==True:
            return True
       else:
            return False
            pass

    def login(self,password):
        if self.password==password:
            return True
        else:
            return False
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
           