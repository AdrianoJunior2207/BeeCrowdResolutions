import math

entrada1 = input("")
entrada1Numeros = entrada1.split()
x1 = float(entrada1Numeros[0])
x2 = float(entrada1Numeros[1])

entrada2 = input("")
entrada2Numeros = entrada2.split()
y1 = float(entrada2Numeros[0])
y2 = float(entrada2Numeros[1])

distance = math.sqrt(pow((x1-y1),2) + pow((y2-x2),2))

print(f"{distance:.4f}")