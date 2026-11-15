"""Conversor de bases numéricas.

Converte um número inteiro para binário, octal ou hexadecimal,
de acordo com a opção escolhida em um menu.

Conceitos: if/elif/else, formatação de strings com format().
"""

BASES = {
    1: ('binário', 'b'),
    2: ('octal', 'o'),
    3: ('hexadecimal', 'X'),
}


def main() -> None:
    numero = int(input('Informe um número inteiro: '))
    opcao = int(input(
        'Escolha a base de conversão:\n'
        '[1] Binário\n'
        '[2] Octal\n'
        '[3] Hexadecimal\n'
        'Sua opção: '
    ))

    if opcao in BASES:
        nome, codigo = BASES[opcao]
        print(f'{numero} em {nome} é {format(numero, codigo)}.')
    else:
        print('Opção inválida. Tente novamente.')


if __name__ == '__main__':
    main()
