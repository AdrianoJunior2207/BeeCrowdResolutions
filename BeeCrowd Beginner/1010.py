firstItem = (input(""))
firstNumber = firstItem.split()
firstNumber1 = int(firstNumber[0])
firstNumber2 = int(firstNumber[1])
firstNumber3 = float(firstNumber[2])

secondItem = (input(""))
secondNumber = secondItem.split()
secondNumber1 = int(secondNumber[0])
secondNumber2 = int(secondNumber[1])
secondNumber3 = float(secondNumber[2])

totalToPay = (firstNumber2 * firstNumber3) + (secondNumber2 * secondNumber3)

print(f"VALOR A PAGAR: R$ {totalToPay:.2f}")
