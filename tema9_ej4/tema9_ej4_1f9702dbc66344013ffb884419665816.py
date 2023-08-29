class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        lista=list(password)
        requisitos=[]
        if len(password)<8:
            return False
        elif len(password)>16:
            return False
        for i in lista:
          if 48<=ord(i)<=57:
            requisitos.append("1")
          elif 32<=ord(i)<47 or 58<=ord(i)<96 or 123<=ord(i)<127:
            requisitos.append("2")
          else:
            requisitos.append("0")
          print(requisitos)
        requisitos="".join(requisitos)
        if requisitos.find("0")!=-1 and requisitos.find("1")!=-1 and requisitos.find("2")!=-1:
            self.password=password
            return True
        else:
            return False

    def login(self,password):
        pl=list(password)
        spl=list(self.password)
        x=set(spl).intersection(pl)
        if len(x)==len(spl):
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
           