class Ciudad:

  def __init__(self,x,y):
      self.x = x
      self.y = y


  def __lt__(self, other):

      if self.x < other.x or self.y < other.y:

          return True

      else:

          return False

  def __eq__(self, other):

      if self.x == other.x or self.y == other.y:

          return True
      else:
          return False

  def __gt__(self, other):

      if self.x>other.x or self.y>other.y:

          return True

      else:

          return False




  def distancia(self,other):

      dx = (other.x-self.x)**2
      dy = (other.y-self.y)**2
      df = (dy+dx)**0.5
      return df

  def camino(self,other):

      pasos = []

      if self.x == other.x:

          if self.y<other.y:

              for i in range(len(other.y-self.y)):

                  if i <= other.y:

                      k = [self.x,i]
                      pasos.append(k)

          if self.y>other.y:

              for i in range(len(self.y-other.y)):

                  if i >= other.y:
                      k = [self.x, i]
                      pasos.append(k)

          else:

              pasos.append([self.x,self.y])

      if self.y == other.y:

          if self.x < other.x:

              for i in range(len(other.x - self.x)):

                  if i <= other.x:
                      k = [i,self.y]
                      pasos.append(k)

          if self.x > other.x:

              for i in range(len(self.x - other.x)):

                  if i >= other.x:

                      k = [i,self.y]
                      pasos.append(k)



      if self.x<other.x:


          for e in range(other.x-self.x):

              if other.y>self.y:

                  for t in range(other.y-self.y):

                      k = [self.x+e,self.y+t]
                      pasos.append(k)

              if self.y>other.y:

                  for w in range(self.y-other.y):

                      k = [self.x+e,self.y-w]


      if self.x>other.x:

          for r in range(self.x-other.x):

              if self.y>other.y:

                  for d in range(self.y-other.y):

                      k = [self.x-r,self.y-d]
                      pasos.append(k)

              elif self.y<other.y:

                  for q in range(other.y-self.y):

                      k = [self.x-r,self.y+q]
                      
      pasos.append([other.x,other.y])
      return pasos
      
      
if __name__ == "__main__":
  pass
         