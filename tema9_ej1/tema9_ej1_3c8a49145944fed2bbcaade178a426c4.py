class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        n=0
        for i in mensaje:
            n+=1
        if n>140:
            print("Solo puedes escribir 140 caracteres")
        b= mensaje.count("#")
        a= mensaje.split(" ")
        for i in a:
            if i[0]=="#":
                self.trending_topics.append(i)
        self.trending_topics= list(set(self.trending_topics))
        return self.trending_topics
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           