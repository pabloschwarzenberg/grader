class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        pass
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)= (hashtag, self.trending_topics[i][1] + 1)
                        encontrado = True
                        break
                if not encontrado:
                    self.trending_topics.append((hashtag, 1))

            # Ordenamos la lista de trending topics por número de menciones
            self.trending_topics.sort(key=lambda x: x[1], reverse=True)

            # Mostramos los tres hashtags más populares
            print("Trending topics:")
            for i in range(min(len(self.trending_topics), 3)):
                print(f"{self.trending_topics[i][0]} ({self.trending_topics[i][1]} menciones)")

        else:
            print("Mensaje demasiado largo")

           