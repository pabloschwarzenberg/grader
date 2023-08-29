class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""  

    def cambiar_password(self,password):
        mayusculas = ["A","B", "C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","V","W","X","Y","Z"]
        signos = ["#","@","$","&","_"]
        numeros = "0123456789"
        a=0
        b=0
        c=0
        z=False
        if 16>=len(password) and len(password)>=8:
            for m in password:
                if m in mayusculas :
                    a=1
                elif m in signos:
                    a=1
                elif m in numeros:
                    b=1000
                if a == 1 and b ==1000:
                    z=True
                    self.password = password
        return z

    def login(self,password):
        if password == self.password:
            d=True
        else:
            d=False
        return d

if __name__ == "__main__":
    usuario=Usuario("pablo","phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("Clavesecreta1"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))
