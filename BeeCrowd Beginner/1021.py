value = float(input(""))

# NOTAS NOTAS NOTAS NOTAS

if value >= 100:
    nota100 = int(value//100)
    value = value%100
else:
    nota100 = 0


if value >= 50:
    nota50 = int(value//50)
    value = value%50
else:
    nota50 = 0
    

if value >=20:
    nota20 = int(value//20)
    value = value%20
else:
    nota20 = 0
    
if value >= 10:
    nota10 = int(value//10)
    value = value%10
else:
    nota10 = 0
    
if value >= 5:
    nota5 = int(value//5)
    value = value%5
else:
    nota5 = 0
    
if value >= 2:
    nota2 = int(value//2)
    value = value%2
else:
    nota2 = 0

# Depois que a que foi feita value%2 o numero fica quebrado tipo 0,7699999 voce
# usa isso para aredondar para 0,77 =D
value = round(value,2)
   
# MOEDAS MOEDAS MOEDAS MOEDAS
value = value*100
if value >= 100:
    moeda1 = int(value/(1*100))
    value = (value%100)
else:
    moeda1 = 0
value = round(value,2)

if value >= 50:
    moeda05 = int(value/(0.5*100))
    value = value%(0.5*100)
else:
    moeda05 = 0
value = round(value,2)   

if value >= 25:
    moeda025 = int(value/(0.25*100))
    value = value%(0.25*100)
else:
    moeda025 = 0
value = round(value,2)   
if value >= 10:
    moeda010 = int(value//(0.1*100))
    value = value%(0.1*100)
else:
    moeda010 = 0
value = round(value,2)  
if value >= 5:
    moeda005 = int(value//(0.05*100))
    value = value%(0.05*100)
else:
    moeda005 = 0
value = round(value,2)   
if value >= 1:
    moeda001 = (value//(0.01*100))
    value%(0.01*100)
    
else:
    moeda001 = 0
    
    
print("NOTAS:")
print(f"{nota100} nota(s) de R$ 100.00")
print(f"{nota50} nota(s) de R$ 50.00")
print(f"{nota20} nota(s) de R$ 20.00")
print(f"{nota10} nota(s) de R$ 10.00")
print(f"{nota5} nota(s) de R$ 5.00")
print(f"{nota2} nota(s) de R$ 2.00")
print("MOEDAS:")
print(f"{moeda1} moeda(s) de R$ 1.00")
print(f"{moeda05} moeda(s) de R$ 0.50")
print(f"{moeda025} moeda(s) de R$ 0.25")
print(f"{moeda010} moeda(s) de R$ 0.10")
print(f"{moeda005} moeda(s) de R$ 0.05")
print(f"{moeda001:.0f} moeda(s) de R$ 0.01")





    
