"""Limite de velocidade.

Recebe a velocidade de um veículo e verifica se ele ultrapassou
o limite de 80 km/h.

Conceitos: if/else, comparação numérica.
"""

LIMITE_KMH = 80


def main() -> None:
    velocidade = float(input('Qual é a velocidade do veículo (km/h)? '))

    if velocidade > LIMITE_KMH:
        print(f'Você ultrapassou o limite de {LIMITE_KMH} km/h e será multado!')
    else:
        print('Parabéns, você está dentro do limite de velocidade!')


if __name__ == '__main__':
    main()
