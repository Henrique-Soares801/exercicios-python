# 🐍 exercicios-python

Exercícios e desafios práticos desenvolvidos durante meus estudos de lógica de programação e Python.
Cada pasta reúne exercícios de um mesmo tema, com nomes de arquivo padronizados em `snake_case`.

## 📁 Estrutura

```
exercicios-python/
└── condicionais/
    ├── alistamento_militar.py
    ├── conversor_bases.py
    ├── entrada_no_brinquedo.py
    ├── formacao_de_triangulo.py
    ├── jogo_de_adivinhacao.py
    ├── limite_de_velocidade.py
    └── prestacao_mensal.py
```

## 🔀 condicionais/

Exercícios focados em estruturas de decisão (`if`, `elif`, `else`) e operadores lógicos.

| Exercício | Descrição | Conceitos |
|---|---|---|
| [`alistamento_militar.py`](condicionais/alistamento_militar.py) | Calcula a idade a partir do ano de nascimento e informa se a pessoa deve se alistar agora, quantos anos faltam ou há quantos anos passou do prazo. | `if/elif/else`, `datetime` |
| [`conversor_bases.py`](condicionais/conversor_bases.py) | Converte um número inteiro para binário, octal ou hexadecimal, conforme a opção escolhida em um menu. | `if/elif/else`, `bin()`, `oct()`, `hex()`, fatiamento de strings |
| [`entrada_no_brinquedo.py`](condicionais/entrada_no_brinquedo.py) | Verifica se a pessoa pode entrar em um brinquedo com altura mínima de 1,40 m. | `if/else`, `float` |
| [`formacao_de_triangulo.py`](condicionais/formacao_de_triangulo.py) | Verifica se três medidas podem formar um triângulo (desigualdade triangular). | `if/else`, operador `and` |
| [`jogo_de_adivinhacao.py`](condicionais/jogo_de_adivinhacao.py) | O computador sorteia um número de 0 a 5 e o jogador tenta adivinhar. | `random.randint`, `time.sleep`, `if/else` |
| [`limite_de_velocidade.py`](condicionais/limite_de_velocidade.py) | Verifica se um veículo ultrapassou o limite de 80 km/h. | `if/else`, comparação numérica |
| [`prestacao_mensal.py`](condicionais/prestacao_mensal.py) | Calcula a prestação mensal de um imóvel e aprova o empréstimo se ela não passar de 30% do salário, validando o prazo informado. | `if/else` aninhados, cálculos financeiros |

## ▶️ Como executar

Requer **Python 3**.

```bash
git clone https://github.com/Henrique-Soares801/exercicios-python.git
cd exercicios-python
python condicionais/alistamento_militar.py
```

Todos os exercícios são interativos e recebem os dados pelo terminal via `input()`.

## 📌 Origem

Estes exercícios foram consolidados a partir de repositórios individuais criados anteriormente, reunindo todo o histórico de estudos em um só lugar.
