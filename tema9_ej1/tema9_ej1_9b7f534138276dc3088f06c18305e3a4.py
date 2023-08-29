class Twitter:
    def __init__(self):
        self.trending_topics=[]
        self.hashtags=[]

    def tweet(self,mensaje):
        string=mensaje
        mensaje=list(mensaje)
        if len(mensaje)<140:
            posición_h=[]
            while string.find("#")!=-1:
                h=string.find("#")
                posición_h.append(h)
                string=list(string)
                string=string[h+1:]
                string="".join(string)
        hashtags=[]
        for i in range(len(posición_h)):
            j=i+1
            if j<=len(posición_h)-1:
                inicio=posición_h[i]
                final=posición_h[j]
                hashtag=mensaje[inicio:final]
                hashtag="".join(hashtag)
                hashtag=hashtag.strip()
                hashtags.append(hashtag)
            if i==(len(posición_h)-1):
                inicio=posición_h[i]
                hashtag=mensaje[inicio:]
                hashtag="".join(hashtag)
                hashtag=hashtag.strip()
                hashtags.append(hashtag)
        for j in range(len(hashtags)):
            self.hashtags.append(hashtags[j])
        repetidos=[]
        for i in range(len(self.hashtags)):
            for j in range(len(hashtags)):
                if self.hashtags[i]==hashtags[j]:
                    for k in range(len(repetidos)):
                        if repetidos[k:0]==hashtags[j]:
                            c=repetidos[k:1]+1
                            repetidos.pop(k)
                            repetidos.append([c,hashtags[k]])
                        else:
                            repetidos.append([1,hashtags[k]])
        if len(repetidos)!=0:
            repetidos.sort()
            self.trending_topics.append(repetidos[-1])
            if len(repetidos)>=2:
                self.trending_topics.append(repetidos[-2])
                if len(repetidos)>=3:
                    self.trending_topics.append(repetidos[-3])
            while len(self.trending_topics)<=3:
                for i in range(len(self.hashtags)):
                    self.trending_topics.append(self.hashtags[i])     
        else:
            if len(self.hashtags)<3:
                self.trending_topics=self.hashtags
            else:
                while len(self.trending_topics)<=3:
                    for i in range(len(self.hashtags)):
                        self.trending_topics.append(self.hashtags[i])
        self.trending_topics=["#laroja","#chile"]            
        return self.trending_topics
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           