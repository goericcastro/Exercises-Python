entrada = input().split()

distancia = int(entrada[0])
diametro1 = int(entrada[1])
diametro2 = int(entrada[2])

if (0 < distancia < 10000) and (0<diametro1<100) and (0<diametro2<100):
    print ("icm:",distancia/(diametro1+diametro2))
