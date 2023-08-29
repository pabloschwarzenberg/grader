class Twitter:
    def __init__(self):
        self.trending_topics=[]
        

    def tweet(self,mensaje):
        self.mensaje=mensaje
        if len(mensaje)>140:
          print("no es valido")
        else:
          pass
        
          
          
        
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print("2")
           