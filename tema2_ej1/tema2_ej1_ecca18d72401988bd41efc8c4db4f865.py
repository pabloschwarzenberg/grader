def sumdiv(Nu):
    sum = 0
    for Div in range(1, Nu):
      if Nu % Div == 0:
            sum += Div
    Primo = sum == 1
    return sum, Primo
if __name__ == "__main__":
  Nu = int(input())
  resu, Primo = sumdiv(Nu)
           