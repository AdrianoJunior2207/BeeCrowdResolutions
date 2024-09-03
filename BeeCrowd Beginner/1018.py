value1 = int(input(""))
value = value1

if value >= 100:
    nota100 = (value//100)
    value = value%100
else:
    nota100 = 0


if value >= 50:
    nota50 = (value//50)
    value = value%50
else:
    nota50 = 0
    

if value >=20:
    nota20 = (value//20)
    value = value%20
else:
    nota20 = 0
    
if value >= 10:
    nota10 = (value//10)
    value = value%10
else:
    nota10 = 0
    
if value >= 5:
    nota5 = (value//5)
    value = value%5
else:
    nota5 = 0
    
if value >= 2:
    nota2 = (value//2)
    value = value%2
else:
    nota2 = 0
    
if value >= 1:
    nota1 = (value//1)
    value = value%1
else:
    nota1 = 0

print(value1)
print(f"{nota100} nota(s) de R$ 100,00")
print(f"{nota50} nota(s) de R$ 50,00")
print(f"{nota20} nota(s) de R$ 20,00")
print(f"{nota10} nota(s) de R$ 10,00")
print(f"{nota5} nota(s) de R$ 5,00")
print(f"{nota2} nota(s) de R$ 2,00")
print(f"{nota1} nota(s) de R$ 1,00")
    
