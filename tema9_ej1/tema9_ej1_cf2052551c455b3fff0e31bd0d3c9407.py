from collections import Counter

class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):

        if len(mensaje) > 140:
            print("Error")
            exit()

        palabras = mensaje.split()
        #print(palabras)

        for i in palabras:
            #print(i)
            if "#" in i:
                self.trending_topics.append(i)
                continue


        top3 = Counter(self.trending_topics)
        print(top3)
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           