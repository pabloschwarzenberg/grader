class Twitter:
    def __init__(self):
        self.trending_topics=[]
        self.trending_counter=[]

    def tweet(self,mensaje):
        if len(mensaje)>140:
            print("Ha superado el límite de caracteres")
            return
        s=0
        l_mensaje=list(mensaje)
        trend_list=[]
        while mensaje.find("#",s)!=-1:
            hashtag=mensaje.find("#",s)
            s=hashtag+1
            u=hashtag
            caracteres=[]
            while u<len(l_mensaje) and l_mensaje[u]!=" ":
                caracteres.append(l_mensaje[u])
                u=u+1
            trend_list.append("".join(caracteres))
        for i in trend_list:
            if i in self.trending_topics:
                pos=self.trending_topics.index(i)
                self.trending_counter[pos]+=1
            else:
                self.trending_topics.append(i)
                self.trending_counter.append(1)
        return
class Topics:
    def __init__(self,topic,number):
        self.topic=topic
        self.number=number
    def __lt__(self, other):
        if self.number<other.number:
            return True
        else:
            return False
    def __repr__(self):
        return str(self.topic)
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    tt=[]
    for u in range(len(twitter.trending_topics)):
        x=Topics(twitter.trending_topics[u],twitter.trending_counter[u])
        tt.append(x)
    tt.sort()
    tt.reverse()
    ss=""
    if len(tt)<3:
        for h in tt:
            ss=ss+h.topic+" "
    else:
        for k in range(3):
            ss=ss+tt[k].topic+" "
    ss=ss
    print(ss)
           