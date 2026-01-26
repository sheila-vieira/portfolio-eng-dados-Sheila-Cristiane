
"""
While

Aqui eu pratiquei o laço while, que repete enquanto uma condição for verdadeira.
Também usei um loop infinito com break para encerrar quando o usuário digita 'x'.
"""

#Ex 1:
num = 1
while num <= 10:
    print(num)
    num += 1
print("Laço encerrado.")

#Ex 2:
while True:
    nome = input("Digite seu nome (ou 'x' para encerrar): ").strip()

    if nome.lower() == 'x':
        break

    if not nome:
        print("Você não digitou nada. Tente novamente.")
        continue

    print(f"Olá, {nome}!")

print("Até logo!")

              