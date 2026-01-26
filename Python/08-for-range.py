
"""
For, range e continue

Aqui eu pratiquei:
- iterar sobre listas e strings com for
- usar range() para gerar sequências numéricas
- usar continue para pular um item específico
"""

#Ex 1:
lista = [1, 2, 3, 4, 5]
for item in lista:
    print(f"Item da lista: {item}")

#Ex 2:
palavra = "Python"
for letra in palavra:
    print(f"Letra: {letra}")

for numero in range(1, 11):  # vai até 10
    print(f"Número atual: {numero}")

#Ex 3:
nome = input('Digite seu nome: ')
for x in range(10):
    print(f"{x+1} - Olá, {nome}!")

#Ex 4:
# range(inicio, fim, passo)
for x in range(2, 20, 2):
    print(x)

for x in range(5, 0, -1):
    print(x)

#Ex 5:
pedras = ("ametista", "quartzo rosa", "jade", "turmalina", "ágata")
for pedra in pedras:
    if pedra == "quartzo rosa":
        continue
    print(pedra)
