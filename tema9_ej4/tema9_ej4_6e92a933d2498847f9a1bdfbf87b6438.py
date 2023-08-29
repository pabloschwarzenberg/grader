class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,pwd):
        if len(pwd)>=8 and len(pwd)<=16:
          num, may, spec=(False,)*3
          for i in pwd:
            if i.isupper():
              may=True
            if i.isdigit():
              num=True
            if not i.isdigit() and not i.isalpha():
              spec=True
          if num and (may or spec):
            self.password=pwd
            return True
        return False
            

    def login(self,pwd):
        if self.password==pwd:
          return True
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
           