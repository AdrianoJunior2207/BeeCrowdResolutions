baseNumbers = input("")
separetedNumbers = baseNumbers.split()
A = float(separetedNumbers[0])
B = float(separetedNumbers[1])
C = float(separetedNumbers[2])
pi = 3.14159

TRIANGULO = (A * C)/2
CIRCULO =  pi * (pow(C,2))
TRAPEZIO = ((A + B) * C)/2
QUADRADO = B * B
RETANGULO = A * B

print(f"TRIANGULO: {TRIANGULO:.3F}")
print(f"CIRCULO: {CIRCULO:.3F}")
print(f"TRAPEZIO: {TRAPEZIO:.3F}")
print(f"QUADRADO: {QUADRADO:.3F}")
print(f"RETANGULO: {RETANGULO:.3F}")
