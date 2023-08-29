class Twitter:
    def __init__(self):
        self.trending_topics=[]
        self.hashtag=[]

    def tweet(self,mensaje):
        self.mensaje=mensaje
        lista=[]
        palabras=mensaje.split(" ")
        if len(mensaje)<=140:
          for palabra in palabras:  
            if palabra[0]=="#":
                i=0
                while i<len(self.hashtag):
                  if self.hashtag[i][0]==palabra:
                    self.hashtag[i][1]+=1
                    break
                  i+=1
                if i==len(self.hashtag): 
                  self.hashtag.append([palabra,1])

        numeros=[]
        self.trending_topics=[]
        for i in self.hashtag:
            numeros.append(int(i[1]))
        print(numeros)
        numeros.sort()
        numeros=numeros[:3]
        for i in self.hashtag:
            for numero in numeros:
                if numero==i[1]:
                    self.trending_topics.append(i[0])
                    break
                    
              
       
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           