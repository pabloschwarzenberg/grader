#Twitter
class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        self.mensaje=mensaje
        #metodo tweet
        if len(self.mensaje)<141: #largo del tweet
          palabras=self.mensaje.split(" ")  #lista que separa los mensajes en sus espacios
          for i in palabras:    #cuenta que va palabra por palabra en la lista palabras
            if i[0]=="#" and ((i in self.trending_topics) == False): #si el primer caracter de una palabra
            #es un '#' y la palabra no se encuentra en los trending topics:
              self.trending_topics.append(i) #a los trending topics se le agregará esa palabra
        i=0
        while i <len(self.trending_topics):
        
            self.trending_topics.count(self.trending_topics[i])      
            i +=1
            
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)