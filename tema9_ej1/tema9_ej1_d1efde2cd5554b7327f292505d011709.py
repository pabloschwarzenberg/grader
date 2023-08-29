class Twitter:
    def __init__(self):
        self.trending_topics=[]
        self.mensaje = ""
        self.hashtags = ""

    def tweet(self,mensaje):
        lista = list(mensaje)
        listaH = []
        if len(lista)<140:
          for i in range (len(lista)):
            if lista[i] == "#":
              for k in range(6):
                if lista[i+k] == " ":
                  for j in range (6):
                    if i+j <= i+k:
                      listaH.append(lista[i+j])
        listaH = "".join(listaH)
        listaH = listaH.split(" ")
        for o in range(len(listaH)):
          self.trending_topics.append(listaH[o])
        pass
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           