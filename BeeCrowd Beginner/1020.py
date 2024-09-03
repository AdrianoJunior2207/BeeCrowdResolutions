days = int(input(""))

if days >= 365:
    anos = days//365
    days = days%365
else:
    anos = 0
    
if days >= 30:
    meses = days//30
    days = days%30
else:
    meses = 0
    
if days >= 1:
    dias = days//1
    days = days%1
else:
    dias = 0
    
print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)")