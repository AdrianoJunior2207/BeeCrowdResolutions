baseNumbers = input("")
separetedNumbers = baseNumbers.split()
A = int(separetedNumbers[0])
B = int(separetedNumbers[1])
C = int(separetedNumbers[2])

maiorAB = (A+B+abs(A-B))/2
maiorGeral = int((C+maiorAB+abs(C-maiorAB))/2)
print(f"{maiorGeral} eh o maior")
