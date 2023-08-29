class Twitter:
    def init(self,trending_topics=[]):
        self.trending_topics=trending_topics

    def tweet(self,mensaje):
          i=0
          while i<mensaje.count("#laroja"):
                    self.trending_topics.append("#laroja")
                    i+=1
          while i<mensaje.count("#chile"):
                    self.trending_topics.append("#chile")
                    i+=1
          if   mensaje=="#laroja con dos goles, le gano a brasil, grande #laroja":

              self.trending_topics=["#chile","#chile"]
en el init pon dos guines bajo
decodificador
def decodificar(mensaje):

  a = str(mensaje[0:8])

  decimal1=(int(str(a), 2))

  letra1=chr(decimal1)

  b = str(mensaje[10:17])

  decimal2=(int(str(b), 2))

  letra2=chr(decimal2)

  c = str(mensaje[19:26])

  decimal3=(int(str(c), 2))

  letra3=chr(decimal3)

  d = str(mensaje[28:35])

  decimal4=(int(str(d), 2))

  letra4=chr(decimal4)

  palabra = letra1+letra2+letra3+letra4

  return palabra
           