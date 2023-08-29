class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        a=0
        for i in password:
          if i!="a" and i!="b" and i!="c" and i!="d" and i!="e" and i!="f" and i!="g" and i!="h" and i!="i" and i!="j" and i!="k" and i!="l" and i!="m" and i!="n" and i!="ñ" and i!="o" and i!="p" and i!="q" and i!="r" and i!="s" and i!="t" and i!="u" and i!="v" and i!="w" and i!="x" and i!="y" and i!="z" and i!=1 and i!=0 and i!=2 and i!=3 and i!=4 and i!=5 and i!=6 and i!=7 and i!=8 and i!=9:
            a=1
        if (len(password)>=8 and len(password)<=16) and a==1:
          self.password=password
          print(True)
        else:
          print(False)
        

    def login(self,password):
        if self.password==password:
          print(True)
        else:
          print(False)
        

if __name__ == "__main__":
    usuario=Usuario("pablo","phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))
           