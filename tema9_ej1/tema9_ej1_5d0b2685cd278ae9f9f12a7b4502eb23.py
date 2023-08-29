class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        self.mensaje=mensaje
        a=self.mensaje.find("#")
        hashtag=""
        while "#" in self.mensaje:        
          for i in self.mensaje[a:]:
            if i !=" ":
              hashtag+=i
            if i==" ":
              break
            lista=[]
            if "#" in self.mensaje:
                for i in self.mensaje:
                    lista.append(i)
                print(lista)
                lista.remove("#")
                self.mensaje="".join(lista)
          if hashtag not in self.trending_topics:
            self.trending_topics.append(hashtag)
            self.trending_topics.append(1)
          else:
            c=0
            for i in self.trending_topics:
              if i == hashtag:
                veces=self.trending_topics.pop(c+1)
                self.trending_topics.insert(c+1,veces+1)
                c+=1
          if len(hashtag)<6:
            c=0
            for i in range(1,len(hashtag)):
              c+=1
              mostrar=print(hashtag[2*c-1])
          else:
            print(hashtag[0])
            print(hashtag[1])
            print(hashtag[2])
            
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           
