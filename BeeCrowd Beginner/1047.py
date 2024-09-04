duracao = input("")
duracaoS = duracao.split()
a = int(duracaoS[0])
b = int(duracaoS[1])
c = int(duracaoS[2])
d = int(duracaoS[3])

if b > d:
    minuto = 60 - b + d
    if a >= c:
        hora = 24 - a + c
    elif a < c:
        hora = c - a
    hora = hora - 1
    
    print(f"O JOGO DUROU {hora} HORA(S) E {minuto} MINUTO(S)")
elif b < d:
    minuto = d - b
    if a > c:
        hora = 24 - a + c
    elif a < c:
        hora = c - a
    elif a == c:
        hora = 0
    print(f"O JOGO DUROU {hora} HORA(S) E {minuto} MINUTO(S)")
elif b == d:
    minuto = 0
    if a > c:
        hora = 24 - a + c
    elif a < c:
        hora = c - a
    elif a == c:
        hora = 24
    print(f"O JOGO DUROU {hora} HORA(S) E {minuto} MINUTO(S)")
