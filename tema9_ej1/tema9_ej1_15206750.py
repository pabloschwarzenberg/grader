class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        contador=0
        for i in mensaje:
            contador+=1
        if contador>140:
            return "exceso de caracteres"
        j=mensaje.strip()
        jj=j.split()
        for i in jj:
            if i[0]=="#" and ((i in self.trending_topics)==False):
                self.trending_topics.append(i)
        print(self.trending_topics)
         
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)

        

if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           