class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self, mensaje):
        mensaje=mensaje.split(" ")
        cantidadpalabras=len(mensaje)
        n=0
        while n<cantidadpalabras:
            if "#" in mensaje[n:0] == True:
                self.trending_topics.append(mensaje[n])
                print(self.trending_topics)

            else:
                n=n+1
                self.mensaje=mensaje


    def trending_topics(self,mensaje):
        i=0
        largolista=len[self.trending_topics]
        cantidaddeveces=[]
        while i<largolista:
            cantidad=self.trending_topics.count(self.trending_topics[i])
            cantidaddeveces.append(cantidad,self.trending_topics[i])
            print(self.trending_topics)
            i=i+1
            cantidaddeveces=cantidaddeveces.sort()
        return cantidaddeveces
        print(cantidaddeveces[0:6])


    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           