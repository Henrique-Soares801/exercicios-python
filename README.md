<div align="center">

# 🐍 Exercícios de Python

**Exercícios práticos de lógica de programação em Python, organizados por tema.**

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-em%20andamento-brightgreen)
![Exercícios](https://img.shields.io/badge/exerc%C3%ADcios-8-blue)

</div>

---

## 📖 Sobre

Este repositório reúne os exercícios que desenvolvo durante meus estudos de Python.
Cada módulo fica em uma pasta numerada, na ordem em que os temas foram estudados, e todos os arquivos seguem o mesmo padrão:

- nomes em `snake_case`;
- código no estilo [PEP 8](https://peps.python.org/pep-0008/);
- docstring explicando o objetivo do exercício;
- função `main()` com `if __name__ == '__main__'`.

## 🗂️ Estrutura

```
exercicios-python/
├── 01_condicionais/
│   ├── alistamento_militar.py
│   ├── conversor_bases.py
│   ├── entrada_no_brinquedo.py
│   ├── formacao_de_triangulo.py
│   ├── gerenciador_de_pagamentos.py
│   ├── jogo_de_adivinhacao.py
│   ├── limite_de_velocidade.py
│   └── prestacao_mensal.py
├── .gitignore
└── README.md
```

## 🔀 01 · Condicionais

Estruturas de decisão (`if`, `elif`, `else`) e operadores lógicos.

| # | Exercício | O que faz | Conceitos |
|:-:|---|---|---|
| 1 | [Entrada no brinquedo](01_condicionais/entrada_no_brinquedo.py) | Verifica se a pessoa tem a altura mínima de 1,40 m. | `if/else`, `float` |
| 2 | [Limite de velocidade](01_condicionais/limite_de_velocidade.py) | Verifica se o veículo passou de 80 km/h. | `if/else`, constantes |
| 3 | [Jogo de adivinhação](01_condicionais/jogo_de_adivinhacao.py) | O computador sorteia um número de 0 a 5 e o jogador tenta acertar. | `random`, `time` |
| 4 | [Formação de triângulo](01_condicionais/formacao_de_triangulo.py) | Diz se três medidas formam um triângulo. | operador `and` |
| 5 | [Alistamento militar](01_condicionais/alistamento_militar.py) | Informa se é hora de se alistar, quanto falta ou quanto passou. | `if/elif/else`, `datetime` |
| 6 | [Prestação mensal](01_condicionais/prestacao_mensal.py) | Aprova o empréstimo se a prestação não passar de 30% do salário. | `if` aninhado, validação |
| 7 | [Conversor de bases](01_condicionais/conversor_bases.py) | Converte um inteiro para binário, octal ou hexadecimal. | `if/elif/else`, `format()` |
| 8 | [Gerenciador de pagamentos](01_condicionais/gerenciador_de_pagamentos.py) | Simula o caixa de uma loja: aplica desconto ou juros conforme a forma de pagamento. | `if/elif/else` aninhados, percentuais |

## 🚀 Como executar

Pré-requisito: [Python 3.8+](https://www.python.org/downloads/).

```bash
git clone https://github.com/Henrique-Soares801/exercicios-python.git
cd exercicios-python
python 01_condicionais/alistamento_militar.py
```

Todos os exercícios são interativos: os dados são digitados no terminal.

## 🛣️ Próximos módulos

- [x] 01 · Condicionais
- [ ] 02 · Laços de repetição
- [ ] 03 · Listas, tuplas e dicionários
- [ ] 04 · Funções

---

<div align="center">

Feito por [Henrique Soares](https://github.com/Henrique-Soares801)

</div>
