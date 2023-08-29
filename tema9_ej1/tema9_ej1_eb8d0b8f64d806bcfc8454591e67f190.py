class Twitter:
    def __init__(self):
        self.trending_topics=[]
        self.hashtags=[]  
        
    def tweet(self,mensaje):
        tp=[]
        caracteres=len(mensaje)
        if caracteres<=140:
           mensaje=mensaje.split(" ")
           for palabra in mensaje:
               if palabra[0]=="#":
                  palabra=list(palabra)
                  palabra.pop(0)
                  palabra="".join(palabra)
                  self.hashtags.append(palabra)
        else:
            return False
        lista=[]
        for hashtag in self.hashtags:
            contar=self.hashtags.count(hashtag)
            l=[hashtag,contar]
            lista.append(l)
        lista.sort()
        p=0
        while p<len(lista)-1:
           if lista[p][0]==lista[p+1][0]:
              lista.pop(p)
              p=1
           else:
                p=p+1
        lista.sort(key=lambda x:x[1], reverse=True)
        if len(lista)>2:
            p=0
            while p<3:
                tp.append(lista[p])
                p=p+1
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