class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        msj=mensaje.split()
        lista=[]
        if len(mensaje)<=140:
            for i in msj:
                for j in i:
                    if j =="#":
                        lista.append(i)
                        contador=lista.count(i)
                        self.trending_topics.append([i,contador])


        else:
            print("Error:excede caracteres")

        

        
        return self.trending_topics
            
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)