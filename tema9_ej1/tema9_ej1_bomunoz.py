#Hito 3

#2)

class Twitter:
    def __init__(self):
    	
        self.trending_topics=[]
        self.hashtags=[]
        self.orden_trending_topics=[]

    def tweet(self,mensaje):
        if len(mensaje)<=140:
        	self.mensaje=mensaje

        lista=[]
        palabras=self.mensaje.split()
        for palabra in palabras:
        	if "#" in palabra:
        		self.hashtags.append(palabra) #Todos los hashtags
	        	if palabra not in self.trending_topics:
	        		self.trending_topics.append(palabra)


        self.lista_count=[]
        for i in self.trending_topics:
        	self.lista_count.append(self.hashtags.count(i))
        
       
        #for i in range(3):
        #	x=self.trending_topics.index(max(self.lista_count))
        #	self.orden_trending_topics.append(self.trending_topics[x])
        #	self.lista_count[x]=0


    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")



    print(twitter.hashtags)
    print(twitter.lista_count)
    print(twitter.trending_topics)
    print(twitter.orden_trending_topics)
           