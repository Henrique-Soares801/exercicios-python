<div align="center">

# 🐍 Exercícios de Python

**Situações do dia a dia transformadas em código: exercícios práticos que registram minha evolução em Python.**

![Python](https://img.shields.io/badge/Python-3-3776AB?logo=python&logoColor=white)
![Módulo atual](https://img.shields.io/badge/m%C3%B3dulo%20atual-condicionais-orange)
![Último commit](https://img.shields.io/github/last-commit/Henrique-Soares801/exercicios-python?label=%C3%BAltima%20atualiza%C3%A7%C3%A3o&color=brightgreen)

</div>

---

## 📖 Sobre

Este repositório registra minha evolução em Python como estudante de Ciência de Dados.
Cada exercício parte de uma situação real, como calcular uma prestação, aplicar um desconto no caixa ou checar um limite de velocidade, e a transforma em um pequeno programa interativo.

**O que você encontra aqui:**

- 🧩 **Problemas práticos:** cada exercício resolve uma situação concreta do cotidiano.
- 📚 **Organização por tema:** as pastas são numeradas na ordem em que estudei cada assunto.
- ✍️ **Código simples e direto:** cada exercício é escrito do jeito que aprendi, sem complicação, para mostrar a lógica de forma clara.
- ▶️ **Pronto para rodar:** basta ter o Python instalado, sem nenhuma biblioteca extra.

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
│   ├── jokenpo.py
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
| 2 | [Limite de velocidade](01_condicionais/limite_de_velocidade.py) | Verifica se o veículo passou de 80 km/h. | `if/else`, comparação numérica |
| 3 | [Jogo de adivinhação](01_condicionais/jogo_de_adivinhacao.py) | O computador sorteia um número de 0 a 5 e o jogador tenta acertar. | `random`, `time` |
| 4 | [Formação de triângulo](01_condicionais/formacao_de_triangulo.py) | Diz se três medidas formam um triângulo. | operador `and` |
| 5 | [Alistamento militar](01_condicionais/alistamento_militar.py) | Informa se é hora de se alistar, quanto falta ou quanto passou. | `if/elif/else`, `datetime` |
| 6 | [Prestação mensal](01_condicionais/prestacao_mensal.py) | Aprova o empréstimo se a prestação não passar de 30% do salário. | `if` aninhado, validação |
| 7 | [Conversor de bases](01_condicionais/conversor_bases.py) | Converte um inteiro para binário, octal ou hexadecimal. | `if/elif/else`, `bin()`, `oct()`, `hex()` |
| 8 | [Gerenciador de pagamentos](01_condicionais/gerenciador_de_pagamentos.py) | Simula o caixa de uma loja: aplica desconto ou juros conforme a forma de pagamento. | `if/elif/else` aninhados, percentuais |
| 9 | [Jokenpô](01_condicionais/jokenpo.py) | Pedra, papel e tesoura contra o computador, com contagem "JO... KEN... PO!!!" antes do resultado. | `if` aninhado, tuplas, `random`, `time` |

## 🚀 Como executar

**1. Instale o Python**

Baixe a versão mais recente em [python.org/downloads](https://www.python.org/downloads/). No Windows, marque a opção **"Add Python to PATH"** durante a instalação.

**2. Baixe os exercícios**

Clone o repositório pelo terminal:

```bash
git clone https://github.com/Henrique-Soares801/exercicios-python.git
cd exercicios-python
```

Ou, sem usar o Git, clique no botão verde **Code → Download ZIP** no topo desta página e extraia a pasta.

**3. Rode o exercício que quiser**

```bash
python 01_condicionais/gerenciador_de_pagamentos.py
```

Troque o nome do arquivo para executar qualquer outro exercício da tabela acima.

**4. Interaja pelo terminal**

Os programas fazem perguntas e respondem na hora. Exemplo:

```
Quanto foi o valor das compras? R$ 1500
FORMAS DE PAGAMENTO:
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
Qual opção? 4
Em quantas parcelas? 10
Sua compra será parcelada em 10x de R$180.00 COM JUROS.
Sua compra de R$1500.00 vai custar R$1800.00 no final.
```

> 💡 Se o comando `python` não for reconhecido no Windows, use `py` no lugar dele.

## 🛣️ Próximos módulos

- [x] 01 · Condicionais
- [ ] 02 · Laços de repetição
- [ ] 03 · Listas, tuplas e dicionários
- [ ] 04 · Funções

---

<div align="center">

Feito por [Henrique Soares](https://github.com/Henrique-Soares801)

</div>
