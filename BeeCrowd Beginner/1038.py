pedidoCliente = (input(""))
pedidoClienteS = pedidoCliente.split()
a = int(pedidoClienteS[0])
b = int(pedidoClienteS[1])

cachorroQuente = 4.00 * b
xSalada = 4.50 * b
xBacon = 5.00 * b
torradaSimples = 2.00 * b
refrigerante = 1.50 * b

if a == 1:
    print(f"Total: R$ {cachorroQuente:.2f}")
elif a == 2:
    print(f"Total: R$ {xSalada:.2f}")
elif a == 3:
    print(f"Total: R$ {xBacon:.2f}")
elif a == 4:
    print(f"Total: R$ {torradaSimples:.2f}")
elif a == 5:
    print(f"Total: R$ {refrigerante:.2f}")

    
    



