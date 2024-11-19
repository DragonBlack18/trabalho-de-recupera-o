# 📐 Calculadora Simples em Python

Este é um projeto de uma **Calculadora Simples** desenvolvida em Python. Este programa permite realizar operações matemáticas básicas entre dois números, como adição, subtração, multiplicação e divisão. Ele foi projetado para ser uma introdução prática aos conceitos de entrada de dados e condicionais em Python.

## ✨ Sobre o Projeto

A calculadora foi desenvolvida com o objetivo de facilitar operações matemáticas simples diretamente no terminal. O programa apresenta uma interface de linha de comando que solicita dois números e um operador, realizando a operação desejada de acordo com o operador inserido.

## ⚙️ Funcionalidades

- 📌 **Adição** (`+`): Soma dois números.
- 📌 **Subtração** (`-`): Subtrai o segundo número do primeiro.
- 📌 **Multiplicação** (`*`): Multiplica dois números.
- 📌 **Divisão** (`/`): Divide o primeiro número pelo segundo, com verificação para evitar divisão por zero.
- 🔄 **Validação de Operador**: Garante que apenas operadores válidos sejam utilizados.
- 🚫 **Tratamento de Erros**: Exibe mensagens de erro para divisão por zero e operadores inválidos.

## 🧩 Estrutura do Código

O código é composto por:

1. **Função `calcular`**: Responsável por processar a operação com base nos números e operador fornecidos.
2. **Entrada de Dados**: Lê os números e o operador do usuário.
3. **Exibição de Resultados**: Exibe o resultado ou uma mensagem de erro caso haja algum problema (como operador inválido ou divisão por zero).

```python
# Função para realizar a operação
def calcular(numero1, numero2, operador):
    if operador == '+':
        return numero1 + numero2
    elif operador == '-':
        return numero1 - numero2
    elif operador == '*':
        return numero1 * numero2
    elif operador == '/':
        if numero2 != 0:
            return numero1 / numero2
        else:
            return "Erro: Divisão por zero"
    else:
        return "Operador inválido"

# Entrada de dados
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operador = input("Digite o operador (+, -, *, /): ")

# Cálculo e exibição do resultado
resultado = calcular(numero1, numero2, operador)
print(f"Resultado: {resultado}")
```
## 📋 Exemplo de Uso
- Digite o primeiro número: 10
- Digite o segundo número: 2
- Digite o operador (`+`), (`-`), (`*`), (`/`): (`/`)
- Resultado: 5.0

## 💡 Possíveis Erros

- Divisão por zero: Caso o usuário insira 0 como segundo número e escolha o operador (`/`), o programa exibirá uma mensagem de erro ao invés de realizar a operação.
- Operador inválido: Se o operador inserido não for um dos esperados (`+`), (`-`), (`*`), (`/`), o programa retornará "Operador inválido".

## 🛠️ Tecnologias Utilizadas

- Python 3.x: Linguagem de programação utilizada para desenvolver a calculadora.

## 🧩 Possíveis Melhorias

- Adicionar suporte para operações mais avançadas (como exponenciação e radiciação).
- Implementar uma interface gráfica usando a biblioteca Tkinter.
- Melhorar o tratamento de erros, exibindo mensagens mais detalhadas para entradas inválidas.
- Adicionar testes unitários para garantir o funcionamento correto das operações.




