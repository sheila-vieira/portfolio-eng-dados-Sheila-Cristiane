
"""
Condicionais (if / elif / else)

Neste exercício eu calculei a média de duas notas e classifiquei o resultado:
- Aprovado (>= 7)
- Recuperação (>= 5 e < 7)
- Reprovado (< 5)
"""

#Ex 1:
n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))

media = (n1 + n2) / 2

if media >= 7:
    print("Resultado: Aprovado")
elif media >= 5 and media < 7:
    print("Resultado: Recuperação")
else:
    print("Resultado: Reprovado")

print("Sua média é {}".format(media))
