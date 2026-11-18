from random import randint
from  time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)

print(''' Suas Opções

[0] PEDRA
[1] PAPEL
[2] TESOURA''')


print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
jogador = int(input(' Qual Deseja Jogar ? '))
print('-='*11)
print(f' O Computador Jogou {itens[computador]}')
print(f' O Jogador Jogou {itens[jogador]}')
print('-='*11)

if computador == 0: #COMPUTADOR JOGOU PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1: #PAPEL
        print('Jogador VENCEU')
    elif jogador == 2: #TESOURA
        print('Computador VENCEU')
    else:
        print('Erro Tente Jogar Novamente!!!')
elif computador == 1: #COMPUTADOR JOGOU PAPEL
    if jogador == 0:
        print(' Computador VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Jogador VENCEU')
    else:
        print('Erro Tente Jogar Novamente!!!')

elif computador == 2:  #COMPUTADOR JOGOU TESOURA
    if jogador == 0:
        print('Jogador VENCEU')
    elif jogador == 1:
        print('Computador VENCEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Erro Tente Novamente!!!')
