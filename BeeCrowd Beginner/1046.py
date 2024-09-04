duracao = input("")
duracaoS = duracao.split()
x = int(duracaoS[0])
y = int(duracaoS[1])

if x > y:
    horaJogada = ((24 - x) + y)
    print(f"O JOGO DUROU {horaJogada} HORA(S)")
elif x < y:
    horaJogada = y - x
    print(f"O JOGO DUROU {horaJogada} HORA(S)")
elif x == y:
    print(f"O JOGO DUROU 24 HORA(S)")