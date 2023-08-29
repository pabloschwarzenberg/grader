
class Twitter:

    def __init__(self,):
        self.trending_topics = []
        self.tweets = []
        self.hashtags = []
    def tt(self):
        if len(self.hashtags) < 3:
            self.trending_topics = self.hashtags[:(len(self.hashtags))]
        else:
            self.trending_topics = self.hashtags[:3]
    def tweet(self,mensaje):
        if len(mensaje) <= 140:
            self.tweets.append(mensaje)
            mensaje = mensaje.split(' ')
            for palabra in mensaje:
                if palabra[0] == '#' and len(self.hashtags) > 0:
                    cont = 0
                    for hs in self.hashtags:
                        if palabra == hs[1]:
                            hs[0] += 1
                            cont += 1
                    if cont == 0:
                        self.hashtags.append([1,palabra])
                elif palabra[0] == '#' and len(self.hashtags) == 0:
                    self.hashtags.append([1,palabra])
            self.hashtags.sort(key=None,reverse=True)
            self.tt()

        else:
            return
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           