valor = float(input('Quanto foi o valor das compras? R$ '))

print('''FORMAS DE PAGAMENTO:
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')

escolha = int(input('Qual opção? '))

if escolha == 1:
    desconto = valor * (10 / 100)
    novovalor = valor - desconto
    print(f'Sua compra de R${valor:.2f} vai custar R${novovalor:.2f} no final.')
elif escolha == 2:
    desconto = valor * (5 / 100)
    novovalor = valor - desconto
    print(f'Sua compra de R${valor:.2f} vai custar R${novovalor:.2f} no final.')
elif escolha == 3:
    parcela = valor / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS.')
    print(f'O valor total da sua compra foi de R${valor:.2f}.')
elif escolha == 4:
    parcelar = int(input('Em quantas parcelas? '))
    if parcelar < 3:
        print('Erro: Para 3x ou mais, escolha pelo menos 3 parcelas.')
    else:
        juros = valor * (20 / 100)
        valorjuros = valor + juros
        par = valorjuros / parcelar
        print(f'Sua compra será parcelada em {parcelar}x de R${par:.2f} COM JUROS.')
        print(f'Sua compra de R${valor:.2f} vai custar R${valorjuros:.2f} no final.')
else:
    print('Erro: Verifique se escolheu corretamente as opções.')
