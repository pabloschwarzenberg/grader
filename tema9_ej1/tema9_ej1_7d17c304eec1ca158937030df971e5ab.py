class Twitter:
	
	def __init__(self):
		
		self.trending_topics=[]

	def tweet(self, mensaje):

		H=self.Buscar(mensaje)

		self.Tendencia(H)

	def Buscar(self, mensaje):
		
		H=[]
		palabras=mensaje.split()
		
		for palabra in palabras:
			
			if palabra.startswith("#"):
				
				comentario=palabra[1:] 
				H.append(comentario)
				
		return H

	def Tendencia(self, H):
		
		for comentario in H:
			
			shakira=False
			
			for topic in self.trending_topics:
				
				if topic[0]==comentario:
					
					topic[1]+=1
					shakira=True
					break
					
			if not shakira:
				
				self.trending_topics.append([comentario, 1])

		self.trending_topics.sort(key=lambda x: x[1], reverse=True)
		self.trending_topics=self.trending_topics[:3]


if __name__=='__main__':
	
	twitter = Twitter()
	twitter.tweet("gano #laroja")
	twitter.tweet("grande #chile")
	twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
	print(twitter.Tendencia_topics)