valores = input().split()

horas = int(valores[0])
velocidad_media = int(valores[1])

litros_combustible = horas * velocidad_media / 12

print(f"{litros_combustible:.3f}")