class Twitter:
    def __init__(self):
        self.trending_topics=[]
        self.hashtags=[]

    def tweet(self,mensaje):
        tp=[]
        caracteres=len(mensaje)
        if caracteres<=140:
          mensaje=mensaje.split(" ")
          for i in mensaje:
            if i[0]=="#":
              i=list(i)
              i.pop(0)
              i="".join(i)
              self.hashtags.append(i)
        lista=[]
        for hashtag in self.hashtags:
          contar=self.hashtags.count(hashtag)
          l1=[hashtag,contar]
          lista.append(l1)
        lista.sort()
        i=0
        while i < len(lista) -1:
          if lista[i][0]==lista[i+1][0]:
            lista.pop(i)
            i=i
          else:
            i+=1
        lista.sort(key=lambda x: x[1],reverse=True)
        if len(lista)>2:
          i=0
          while i<3:
            tp.append(lista[i])
            i+=1
        if len(lista)==2:
          tp.append(lista[0])
          tp.append(lista[1])
        if len(lista)==1:
          tp.append(lista[0])
        self.trending_topics=tp
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)