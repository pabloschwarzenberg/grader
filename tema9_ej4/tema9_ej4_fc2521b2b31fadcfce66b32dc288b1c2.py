class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        password
        seguir=""
        continuar=""
        lista=["0","1","2","3","4","5","6","7","8","9"]
        listaB=["!","#","%","&","/","(",")","=","?","¡","¿","*","+","_"]
        for i in lista:
            if password.find(i)!=-1:
                seguir="si"
                break
        if password!=password.lower():
            continuar="si"
        for i in listaB:
            if password.find(i)!=-1:
                continuar="sisi"
                break
        password=list(password)
        if seguir=="si" and (continuar=="si" or continuar=="sisi") and len(password)>=8 and len(password)<=16:
            self.password=password
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
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))
           