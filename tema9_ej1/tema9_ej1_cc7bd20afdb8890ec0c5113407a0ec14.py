class Twitter:
    def __init__(self):
    
        self.trending_topics=[]

    def tweet(self, mensaje):
        if len(mensaje) > 140:
            return False
        else:
            for posicion in range(0,len(mensaje)):
                if mensaje[posicion] == "#":
                    hashtag = []
                    for i in range(posicion, len(mensaje)):
                        if mensaje[i] == " ":
                            break
                        hashtag.append(mensaje[i])
                    hashtag = "".join(hashtag)
                    if hashtag not in self.trending_topics:
                        self.trending_topics.append(hashtag)