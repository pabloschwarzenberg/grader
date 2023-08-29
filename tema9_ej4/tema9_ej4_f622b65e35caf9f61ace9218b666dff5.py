class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        abcedario=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        numeros=["1","2","3","4","5","6","7","8","9","0"]
        largo=len(password)
        if largo<8 or largo>16:
            Largo=False
        else:
            Largo=True
        clave=password
        password2=list(clave)
        for i in password2:
            for numero in numeros:
                if i==numero:
                    password2.remove(i)
        password2="".join(password2)
        if password2==clave:
            y1=False
        else:
            y1=True

            
        password3=list(password)
        password4=list(password)
        password1ower=password.lower()
        if password1ower==password:
            for j in password3:
                for letra in abcedario:
                    if j==letra:
                        password4.remove(j)
                for numero in numeros:
                    if j==numero:
                        password4.remove(j)
            if len(password4)==0:
                x1=False
            else:
                x1=True
        else:
            x1=True
            
        if Largo and x1 and y1 and Largo:
            self.password=password
            return True
        
        else:
            return False
        

    def login(self,password):
        if password==self.password:
            return True
        else:
            return False
if __name__ == "__main__":
    usuario=Usuario("pablo","phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))#False
    print(usuario.cambiar_password("clavesecreta1_"))#True
    print(usuario.cambiar_password("clavesecreta"))#False
    print(usuario.cambiar_password("clasesecreta1"))#False
    print(usuario.cambiar_password("claveSecreta1"))#False
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))