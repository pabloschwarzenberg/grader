class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, mensaje):
        l=list(mensaje)
        pos1 =[]
        pos2 =[]
        if len(mensaje) <= 140:
            for i in range(len(l)):
                if mensaje[i] is "#":
                    pos1.append(i)
                if mensaje[i] is " ":
                    pos2.append(i)
        for i in range(len(pos1)):
            for j in range(len(pos2)):
                if pos1[i]< pos2[j] and pos2[j+1]
        print(pos1,pos2)

if __name__ == "__main__":
    twitter = Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
