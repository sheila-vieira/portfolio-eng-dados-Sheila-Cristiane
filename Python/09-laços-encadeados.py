'''Laços encadeados 

Aqui pratiquei um laço dentro de outro para criar repetições em níveis:
o laço externo controla as rodadas/conjuntos e o interno executa ações
dentro de cada rodada (contagem regressiva e geração de números aleatórios).
'''
#Ex 1: 
for cont_ex in range(1,6):
    print(f'\nRodada: {cont_ex}')
    for cont_in in range(5,0,-1):
        print(f'Valor: {cont_in}')
print('Fim dos laços')

#Ex:2
import random

for A in range (1,6):
    print(f'\Conjunto {A}')
    for B in range(5):
        num = random.randint(1,100)
        print(f'Valor: {num}')

