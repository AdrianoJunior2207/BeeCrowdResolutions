time = int(input(""))

if time >= 3600:
    hora = time//3600
    time = time%3600
else:
    hora = 0
    
if time >= 60:
    minuto = time//60
    time = time%60
else:
    minuto = 0
    
if time >= 1:
    segundo = time//1
    time = time%1
else:
    segundo = 0
    
print(f"{hora}:{minuto}:{segundo}")
    