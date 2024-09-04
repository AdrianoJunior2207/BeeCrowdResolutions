numerosJ = input("")
numerosS = numerosJ.split()
a = float(numerosS[0]) 
b = float(numerosS[1]) 
c = float(numerosS[2]) 
d = float(numerosS[3]) 

n1 = a*2
n2 = b*3
n3 = c*4
n4 = d*1

media = (n1+n2+n3+n4)/10
if media >= 7:
   print(f"Media: {media:.1f}")
   print("Aluno aprovado.")
elif media < 5:
    print(f"Media: {media:.1f}")
    print("Aluno reprovado.")
elif media >= 5 and media < 6.9:
    print(f"Media: {media:.1f}")
    print("Aluno em exame.")
    exame = float(input(""))
    mediaF = float(media + exame)/2
    if mediaF >= 5:
        print(f"Nota do exame: {exame:.1f}")
        print("Aluno aprovado.")
        print(f"Media final: {mediaF:.1f}")
    elif mediaF <= 4.9:
        print(f"Nota do exame: {exame:.1f}")
        print("Aluno reprovado.")
        print(f"Media final: {mediaF:.1f}")
    



    
    
    