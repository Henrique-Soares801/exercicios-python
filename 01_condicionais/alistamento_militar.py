"""Alistamento militar.

Calcula a idade do usuário a partir do ano de nascimento e informa
se ele deve se alistar agora, quantos anos faltam ou há quanto tempo
o prazo de alistamento passou.

Conceitos: if/elif/else, módulo datetime.
"""

from datetime import date

IDADE_ALISTAMENTO = 18


def main() -> None:
    ano_atual = date.today().year
    ano_nascimento = int(input('Informe o ano em que você nasceu: '))
    idade = ano_atual - ano_nascimento

    print(f'Quem nasceu em {ano_nascimento} tem {idade} anos em {ano_atual}.')

    if idade == IDADE_ALISTAMENTO:
        print('Você deve se alistar IMEDIATAMENTE!')
    elif idade < IDADE_ALISTAMENTO:
        saldo = IDADE_ALISTAMENTO - idade
        print(f'Ainda faltam {saldo} ano(s) para o seu alistamento.')
        print(f'Seu alistamento será em {ano_atual + saldo}.')
    else:
        saldo = idade - IDADE_ALISTAMENTO
        print(f'Você deveria ter se alistado há {saldo} ano(s).')
        print(f'Seu alistamento foi em {ano_atual - saldo}.')


if __name__ == '__main__':
    main()
