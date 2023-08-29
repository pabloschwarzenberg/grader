class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
      if 8<=len(password) and len(password)<=16:
        mayus=False
        num=False
        carac="!#$%&/()=?¡_-.:,;"
        esp=False
        for i in password:
          if i==i.upper():
            mayus=True
          elif i in carac:
            esp=True
          elif i.isdigit()==True:
            num=True
        if num==True and esp==True and mayus==True:
          return True
          self.password=password
        else:
          return False
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
    print(usuario.login("claveSecreta1"))
           