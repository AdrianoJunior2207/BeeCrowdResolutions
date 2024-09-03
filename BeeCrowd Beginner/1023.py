variaveisJ = (input(""))
variaveisS = variaveisJ.split()

a = float(variaveisS[0])
b = float(variaveisS[1])
c = float(variaveisS[2])

delta = float((b**2)-4*a*c)
if delta > 0 and a != 0:
    x1 = (-b+(pow(delta,0.5))) / (2*a)
    x2 = (-b-(pow(delta,0.5))) / (2*a)
    print(f"R1 = {x1:.5f}")
    print(f"R2 = {x2:.5f}")
else:
    print(f"Impossivel calcular")

    

    
