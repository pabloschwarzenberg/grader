class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        if password=="clave":
          return False
        if 8<=len(password)<=16:
          list1=list("1234567890")
          list2=list("abcdefghijklmnopqrstuvwxyz")
          list3=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
          Y=list(password)
          count1=0
          for i in range(0,len(list1)):
            if password.find(list1[i])!=-1:
              Y.remove(list1[i])
              count1=count1+1
          if count1!=0:
            count2=0
            for j in range(0,len(list2)):
              while str(Y).find(list2[j])!=-1:
                x=int(len(Y))
                Y.remove(list2[j])
                count2=count2+1
            if count2!=0:
              if len(Y)!=0:
                return True
              else:
                return False
          return False
        else:
          return True

    def login(self,password):
        if str(self.password)!=str(password):
          return False
        else :
          return True

if __name__ == "__main__":
    usuario=Usuario("pablo","phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))
           