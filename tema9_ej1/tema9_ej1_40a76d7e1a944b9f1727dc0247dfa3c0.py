class Twitter:
    def __init__(self,trending_topics=[]):
        self.trending_topics=trending_topics

    def tweet(self,mensaje):
            #mensaje="#laroja con dos goles, le gano a brasil, grande #laroja"

            s = 'this_is_a_twitter etiqueta #';
            s = s.find ("#")
            print(s)

            for i in mensaje:
               if i=="#":    
                   self.trending_topics=["#chile","#chile"]
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           