class Twitter:
    def __init__(self):
        self.trending_topics=[]
        self.ttstring = []

    def tweet(self,mensaje):
        if len(mensaje) <= 140:
            palabras = mensaje.split()

            for i in range(len(palabras)):
                if palabras[i][0] == '#':
                    if palabras[i] not in self.ttstring:
                        self.trending_topics.append([palabras[i], 1])
                        self.ttstring.append(palabras[i])
                    else:
                        ind = self.ttstring.index(palabras[i])
                        self.trending_topics[ind][1] += 1