class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        abc="abcdefghijklmnopqrstuvwxyz"
        ABC=abc.upper()
        n="1234567890"
        if 8<=len(password)<=16:
          for i in abc:
            if password.find(i)!=-1:
              for u in n:
                if u==n[len(n)-1] and password.find(u)==-1:
                  return False
                if password.find(u)!=-1:
                  for l in ABC:
                    if password.find(l)!=-1:
                      self.password=password
                      return True
                  for x in password:
                    if abc.find(x)==-1 and ABC.find(x)==-1 and n.find(x)==-1:
                      self.password=password
                      return True
                    if x==password[len(password)-1] and abc.find(x)!=-1 and ABC.find(x)!=-1 and n.find(x)!=-1: 
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
           