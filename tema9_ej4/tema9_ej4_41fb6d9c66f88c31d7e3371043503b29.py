class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        abcdario = "abcdefghijklmnopqrstuvwxyz"
        nros = "0123456789"
        abcdarioupp = abcdario.upper()
        z=0
        x=0
        c=0
        v=0
        if 8<=len(str(password))<=16:
          for n in password:
            if abcdario.find(n)!=-1:
              z+=1
            elif nros.find(n)!=-1:
              x+=1
            elif abcdarioupp.find(n)!=-1:
              c+=1
            elif abcdario.find(n)==-1 and nros.find(n)==-1 and abcdarioupp.find(n)==-1:
              v+=1
        if z>0 and x>0 and (c>0 or v>0):  
            self.password = password
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
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))
           