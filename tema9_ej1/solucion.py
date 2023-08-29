class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        palabras_con_hashtag=[]
        repeticiones=[]
        palabras=mensaje.split()
        for palabra in palabras:
            if palabra[0]=="#":
                encontrado=False
                for i in range(len(self.trending_topics)):
                    if palabra == self.trending_topics[i][1]:
                        self.trending_topics[i][0]+=1
                        encontrado=True
                        break
                if not encontrado:
                    self.trending_topics.append([1,palabra])

        self.trending_topics.sort(reverse=True)

if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja le gano a brasil")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
