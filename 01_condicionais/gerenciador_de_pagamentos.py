"""Gerenciador de pagamentos.

Simula o caixa de uma loja: calcula o valor final de uma compra de
acordo com a forma de pagamento escolhida pelo cliente.

- À vista (dinheiro/cheque): 10% de desconto
- À vista no cartão: 5% de desconto
- 2x no cartão: sem juros
- 3x ou mais no cartão: 20% de juros sobre o total

Conceitos: if/elif/else, condicionais aninhadas, cálculos percentuais.
"""

DESCONTO_DINHEIRO = 0.10
DESCONTO_CARTAO = 0.05
JUROS_PARCELADO = 0.20
MINIMO_PARCELAS_COM_JUROS = 3


def main() -> None:
    valor = float(input('Quanto foi o valor das compras? R$ '))

    print('''FORMAS DE PAGAMENTO:
[1] À vista dinheiro/cheque
[2] À vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')

    escolha = int(input('Qual opção? '))

    if escolha == 1:
        valor_final = valor * (1 - DESCONTO_DINHEIRO)
        print(f'Sua compra de R$ {valor:.2f} vai custar R$ {valor_final:.2f} no final.')
    elif escolha == 2:
        valor_final = valor * (1 - DESCONTO_CARTAO)
        print(f'Sua compra de R$ {valor:.2f} vai custar R$ {valor_final:.2f} no final.')
    elif escolha == 3:
        parcela = valor / 2
        print(f'Sua compra será parcelada em 2x de R$ {parcela:.2f} SEM JUROS.')
        print(f'O valor total da sua compra foi de R$ {valor:.2f}.')
    elif escolha == 4:
        parcelas = int(input('Em quantas parcelas? '))
        if parcelas < MINIMO_PARCELAS_COM_JUROS:
            print(f'Erro: para esta opção, escolha pelo menos {MINIMO_PARCELAS_COM_JUROS} parcelas.')
        else:
            valor_final = valor * (1 + JUROS_PARCELADO)
            parcela = valor_final / parcelas
            print(f'Sua compra será parcelada em {parcelas}x de R$ {parcela:.2f} COM JUROS.')
            print(f'Sua compra de R$ {valor:.2f} vai custar R$ {valor_final:.2f} no final.')
    else:
        print('Erro: opção inválida. Escolha uma opção de 1 a 4.')


if __name__ == '__main__':
    main()
