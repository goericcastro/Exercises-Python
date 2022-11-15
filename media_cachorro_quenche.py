valores = input().split() 

h = int(valores[0])
p = int(valores[1])

if (1<=h) and (p<=1000):
  media = h/p
  print(f"{media:.2f}")