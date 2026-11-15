"""Formação de triângulo.

Verifica se três medidas podem formar um triângulo, aplicando a
condição de existência (desigualdade triangular).

Conceitos: if/else, operador lógico and.
"""


def main() -> None:
    lado1 = float(input('Informe a medida do primeiro lado: '))
    lado2 = float(input('Informe a medida do segundo lado: '))
    lado3 = float(input('Informe a medida do terceiro lado: '))

    if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
        print('É possível formar um triângulo.')
    else:
        print('Não é possível formar um triângulo.')


if __name__ == '__main__':
    main()
