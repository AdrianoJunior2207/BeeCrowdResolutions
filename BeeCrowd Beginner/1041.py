coordenada = input("")
coordenadaS = coordenada.split()
x = float(coordenadaS[0])
y = float(coordenadaS[1])

if x > 0 and y > 0:
    print("Q1")
elif x < 0 and y > 0:
    print("Q2")
elif x < 0 and y < 0:
    print("Q3")
elif x > 0 and y < 0:
    print("Q4")  
elif x == 0 and (y > 0 or y < 0):
    print("Eixo Y") 
elif y == 0 and (x > 0 or x < 0):
    print("Eixo X") 
elif x == 0 or y == 0:
     print("Origem")
