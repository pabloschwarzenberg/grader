class Usuario:
    def __init__(self,nombre,email,):
        self.nombre=nombre
        self.email=email
        self.password=""

    def cambiar_password(self,password):
        clave=password
        if len(clave)<8 or len(clave)>16:
          return False
        else:
          numeros='1234567890'
          num=[]
          for i in range(len(numeros)):
              nume=numeros[i]
              num.append(nume)
          letras='qwertyuiopasdfghjklñzxcvbnm'
          letra=[]
          for i in range(len(letras)):
              let=letras[i]
              letra.append(let)
          mayus='QWERTYUIOPÑLKJHGFDSAZXCVBNM'
          may=[]
          for i in range(len(mayus)):
              mayu=mayus[i]
              may.append(mayu)
          simbol='!·$%&/()?¿_\|@#~~€¬º'
          sim=[]
          for i in range(len(simbol)):
              simb=simbol[i]
              sim.append(simb)

          caracteres=[]
          for i in range(len(clave)):
              caracter=clave[i]
              caracteres.append(caracter)

          for i in range(len(caracteres)):
              a=caracteres[i]
              if (a in sim):
                   simbol=True
              elif(a in may):
                  mayus=True
              elif (a in letra):
                  letras=True
              elif (a in num):
                  numeros=True
              
          if (simbol==True or mayus==True) and (letras)==True and (numeros)==True:
              return True
          else:
              return False
        return clave
        

    def login(self,password1):
        clave=self.password
        if clave !=password1:
            return False
        else:
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