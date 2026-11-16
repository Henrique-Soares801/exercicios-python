num = int(input(' Informe um Número Inteiro Qualquer: '))
base = int(input(' Escolha Qual Será a Base de Conversão:\n'
                 '[1] Converter Para Binário\n'
                 '[2] Converter Para Octal\n'
                 '[3] Converter Para Hexadecimal\n'
                 'Sua Opção: '))

if base == 1:
    print(f' Você Escolheu Converter Para Binário o Número {num} em Binário é {format(num, 'b')} ')
elif base == 2:
    print(f' Você Escolheu Converter Para Octal o Número {num} em Octal é {format(num, 'o')} ')
elif base == 3:
    print(f' Você Escolheu Converter Para HexaDecimal o Número {num} em HexaDecimal é {format(num, 'x')} ')
else:
    print(' Opção Inválida Tente Novamente!')