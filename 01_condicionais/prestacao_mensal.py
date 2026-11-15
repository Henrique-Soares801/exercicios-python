"""Prestação mensal.

Calcula a prestação mensal para a compra de uma casa e aprova o
empréstimo somente se ela não ultrapassar 30% do salário.

Conceitos: if/else aninhados, validação de entrada.
"""

PERCENTUAL_MAXIMO = 0.30


def main() -> None:
    valor_casa = float(input('Qual é o valor da casa? R$ '))
    salario = float(input('Qual é o seu salário mensal? R$ '))
    anos = int(input('Em quantos anos você pretende pagar? '))

    if anos > 0:
        prestacao = valor_casa / (anos * 12)
        limite = salario * PERCENTUAL_MAXIMO

        if prestacao <= limite:
            print('Empréstimo aprovado!')
        else:
            print('Empréstimo negado!')

        print(f'Sua prestação mensal ficará em R$ {prestacao:.2f}.')
    else:
        print('O prazo precisa ser maior que zero!')


if __name__ == '__main__':
    main()
