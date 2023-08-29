import math
class Ciudad:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.route=[]
    def distancia(self,p2):
        return math.sqrt((self.x-p2.x)**2+(self.y-p2.y)**2)
    def camino(self,p2):
        self.route.append([self.x,self.y])
        a=self.x
        b=self.y
        if p2.x>a and p2.y>b:
            while a<p2.x and b<p2.y:
                a+=1
                b+=1
                self.route.append([a,b])
            while a<p2.x and b==p2.y:
                a+=1
                self.route.append([a,b])
            while a==p2.x and b<p2.y:
                b+=1
                self.route.append([a,b])
        if p2.x<a and p2.y>b:
            while a>p2.x and b<p2.y:
                a-=1
                b+=1
                self.route.append([a,b])
            while a>p2.x and b==p2.y:
                a-=1
                self.route.append([a,b])
            while a==p2.x and b<p2.y:
                b+=1
                self.route.append([a,b])
        if p2.x>a and p2.y<b:
            while a<p2.x and b>p2.y:
                a+=1
                b-=1
                self.route.append([a,b])
            while a<p2.x and b==p2.y:
                a+=1
                self.route.append([a,b])
            while a==p2.x and b>p2.y:
                b-=1
                self.route.append([a,b])
        if p2.x==a and p2.y>b:
            while a==p2.x and b<p2.y:
                b+=1
                self.route.append([a,b])
        if p2.x==a and p2.y<b:
            while a==p2.x and b>p2.y:
                b-=1
                self.route.append([a,b])
        if p2.x<a and p2.y==b:
            while a>p2.x and b==p2.y:
                a-=1
                self.route.append([a,b])
        if p2.x>a and p2.y==b:
            while a<p2.x and b==p2.y:
                a+=1
                self.route.append([a,b])
        return self.route

if __name__ == "__main__":
  pass
         