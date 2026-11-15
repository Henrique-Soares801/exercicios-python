"""Jogo de adivinhação.

O computador sorteia um número de 0 a 5 e o jogador tenta adivinhar.

Conceitos: if/else, módulos random e time.
"""

from random import randint
from time import sleep


def main() -> None:
    numero_sorteado = randint(0, 5)
    palpite = int(input('Adivinhe o número que eu pensei (de 0 a 5): '))

    print('Pensando...')
    sleep(3)

    if palpite == numero_sorteado:
        print('Parabéns, você acertou!')
    else:
        print(f'Você errou! O número era {numero_sorteado}.')


if __name__ == '__main__':
    main()
