
"""
Operadores Lógicos (and, or, not)

Neste exercício eu pratiquei como combinar condições booleanas para tomar decisões.
Usei AND para exigir duas condições verdadeiras, OR para aceitar uma delas,
e NOT para inverter um valor booleano.
"""

#Ex 1:
idade = 19
altura = 1.75

resultado = idade >= 18 and altura >= 1.70
print("A pessoa é maior de idade e tem altura suficiente:", resultado)

resultado = idade < 18 or altura < 1.70
print("A pessoa é menor de idade ou tem altura insuficiente:", resultado)

# Programa de disparo de alarme
porta = 'f'
janela = 'a'

alarme = (porta == 'a' or janela == 'a')
print("Disparar alarme:", alarme)

# Programa de compra (uso do NOT)
tem_dinheiro = False
tem_dinheiro = not tem_dinheiro
msg = 'Tem dinheiro para comprar? ' + str(tem_dinheiro)
print(msg)
