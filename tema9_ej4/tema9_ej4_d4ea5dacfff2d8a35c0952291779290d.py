class Twitter:
    def __init__(self):
        self.trending_topics=[]
    def tweet(self,mensaje):
        if len(mensaje)>140:
          return ("El máximo de caracteres es de 140")
        lista=mensaje.split()
        lista1=[]
        for i in lista:
          if i[0]=="#":
            self.trending_topics.append(i)
            for i in self.trending_topics:
              if self.trending_topics.count(i)>1:
                self.trending_topics.remove(i)
      

        return 
          
   

if __name__ == "__main__":
    usuario=Usuario("pablo","phschwarzenberg@uc.cl")
    print(usuario.cambiar_password("clave"))
    print(usuario.cambiar_password("clavesecreta1_"))
    print(usuario.cambiar_password("clavesecreta"))
    print(usuario.cambiar_password("clasesecreta1"))
    print(usuario.cambiar_password("claveSecreta1"))
    print(usuario.login("clavesecreta1_"))
    print(usuario.login("claveSecreta1"))
           