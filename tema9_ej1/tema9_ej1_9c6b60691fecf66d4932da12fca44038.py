class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        if len(mensaje)<=140:
            i=0
            while i<len(mensaje):
                pos_hash=mensaje.find("#")
                if pos_hash!=-1:
                    mensaje_lista=list(mensaje)
                    if " " in mensaje_lista[pos_hash:]:
                        a=mensaje_lista.index(" ",pos_hash)
                        hashtag=mensaje[pos_hash:a]
                    else:
                        hashtag=mensaje[pos_hash:]
                    self.trending_topics.append(hashtag)
                    i+=1
                
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           
           