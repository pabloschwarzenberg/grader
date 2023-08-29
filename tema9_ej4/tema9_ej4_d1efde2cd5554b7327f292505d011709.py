class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        if len(password)>7 and len(password)<15:
            lista = list(password)
            alpha = 0
            mayus = 0
            digit = 0
            otros = 0
            for i in range(len(lista)-1):
                if lista[i].isalpha:
                    alpha += 1
                    if lista[i].upper() == lista[i]:
                        mayus += 1
                elif lista[i].isdigit:
                    digit += 1
                else:
                    otros += 1
            if mayus>0 or otros>0:
                self.password = password
                return True
            else:
                return False
        else:
            return False

    def login(self,password):
      if self.password == password:
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
           