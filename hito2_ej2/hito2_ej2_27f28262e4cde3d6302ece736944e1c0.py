      def numero_perfecto(a):
  sumaDivisores = 0;
  for i in range(1,a):
    r=a % i
    if(r==0) :
      sumaDivisores += i;

  if sumaDivisores == a :
    return True
  else:
    return False

if __name__ == "__main__":
    a=int(input("Ingrese a:"))
    print(numero_perfecto(a))