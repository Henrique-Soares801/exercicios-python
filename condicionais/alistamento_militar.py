from datetime import date


ano_atual = date.today().year
ano_nasc = int(input('Informe o ano em que você nasceu: '))
idade = ano_atual - ano_nasc


print(f'Quem nasceu em {ano_nasc} tem {idade} anos em {ano_atual}.')


if idade == 18:
    print('Você deve se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    ano_alistamento = ano_atual + saldo
    print(f'Ainda faltam {saldo} anos para você se alistar.')
    print(f'Seu alistamento será no ano de {ano_alistamento}.')
else:
    saldo = idade - 18
    ano_alistamento = ano_atual - saldo
    print(f'Já era para você ter se alistado há {saldo} anos.')
    print(f'Seu alistamento foi em {ano_alistamento}.')


