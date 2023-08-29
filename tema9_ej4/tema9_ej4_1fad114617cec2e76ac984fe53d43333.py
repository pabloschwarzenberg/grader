class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        if len(password)>=8 and len(password)<=16:
            M=0#mayuscula
            S=0#simbolo
            N=0#numero
            Mi=0#minuscula
            for i in password:
                if i>"A":
                    Mi+=1
                if i>"1" and i<"a":
                    M+=1
                if i<"1":
                    S+=1
                if i=="1" or i=="2" or i=="3" or i=="4" or i=="5" or i=="6" or i=="7"or i=="8" or i=="9" or i=="0":
                    N+=1
            if M>0 or S>0:
                if Mi>0 and N>0:
                    self.password=password
                    return True
            else:
                return False
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
           