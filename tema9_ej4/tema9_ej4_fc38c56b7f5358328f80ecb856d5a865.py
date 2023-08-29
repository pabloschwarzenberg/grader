class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        if 8<= len(password)<=16:
           numero=False
           letra=False
           simbolo=False
           for p in password:
              if p.isdigit():
                 numero=True
              if p.isalpha():
                 letra=True
              if not p.isalnum() or (p.upper()==p and not p.isdigit()):
                 simbolo=True
           if numero and letra and simbolo:
              self.password=password
              return True
        return False
            

    def login(self,password):
        if password==self.password:
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
           