class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
      if len(password)>=8 and len(password)<=16:
        x=password
        minusculas="abcdefghijklmnopkrstuvwxyz"
        mayusculas="ABCDEFGHIJKLMNOPKRSTUVWXYZ"
        numeros="1234567890"
        minu=0
        minu1=1
        may=0
        may1=1
        num=0
        num1=1
        for letra in x:
            if letra in minusculas:
                minu=minu+1
            else:
                if letra not in mayusculas and letra not in numeros:
                    minu1=0
                else:
                    minu1=minu1
        for letra in x:
            if letra in mayusculas:
                may=may+1
            else:
                may1=0
        for letra in x:
            if letra in numeros:
                num=num+1
            else:
                num1=0
        if minu!=0 and num!=0:
            if may!=0 or minu1==0:
              return True
              self.password=password
            else:
              self.password=""
              return False
        else:
            self.password=""
            return False
      else:
        self.password=""
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
           