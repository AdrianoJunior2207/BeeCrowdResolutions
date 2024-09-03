variaveisJ = (input(""))
variaveisS = variaveisJ.split()

A = int(variaveisS[0])
B = int(variaveisS[1])
C = int(variaveisS[2])
D = int(variaveisS[3])

if B > C and D > A and ((C + D) > (A + B)) and C > 0 and D > 0 and (A%2==0):
    print(f"Valores aceitos")
else:
    print(f"Valores nao aceitos")