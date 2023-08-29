class Vector3D:
      def __init__(self,x=0,y=0,z=0):
          self.x=x
          self.y=y
          self.z=z
      def modulo(self,v):
          return (((v.x)**2)+((v.y)**2)+((v.z)**2))**(1/2)
      def __add__(self,otro):
          return(suma_vectores(self,otro))         
def suma_vectores(v1,v2):
    return(Vector3D(v1.x+v2.x,v1.y+v2.y,v1.z+v2.z))
           