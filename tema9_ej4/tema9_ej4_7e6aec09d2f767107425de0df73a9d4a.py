class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
        self.password=[]

    def cambiar_password(self,password):
        abecedario = ("abcdefghijklmnopqrstuvwxyz")
        ABECEDARIO = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        numeros = ("0123456789")
        contador1 = 0
        contador2 = 0
        contador3 = 0
        contador4 = 0
        for i in password:
            if i in abecedario:
              contador1+=1
            elif i in ABECEDARIO:
              contador2+=1
            elif i in numeros:
              contador3+=1
            elif i not in abecedario or ABECEDARIO or numeros and i!= " ":
              contador4 +=1
        if contador1 and contador2 != 0 and contador3 or contador4 !=0:
             if 8 <= len(password)<= 16:
                return True
        else:
            return False
          

    def login(self,password):
      if password == self.password:
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
           