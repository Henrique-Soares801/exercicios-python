"""Entrada no brinquedo.

Verifica se a pessoa tem a altura mínima de 1,40 m para entrar
em um brinquedo do parque.

Conceitos: if/else, números de ponto flutuante.
"""

ALTURA_MINIMA = 1.40


def main() -> None:
    altura = float(input('Qual é a sua altura (em metros)? '))

    if altura >= ALTURA_MINIMA:
        print('Entrada permitida. Divirta-se!')
    else:
        print(f'Entrada não permitida. A altura mínima é {ALTURA_MINIMA:.2f} m.')


if __name__ == '__main__':
    main()
