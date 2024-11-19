# 🏗️ Pirâmide com Parâmetro

Este projeto é um simples script em Python que imprime uma pirâmide numérica com base no número de linhas fornecido pelo usuário. 🐍✨ A pirâmide é construída com números crescentes em cada linha.

## ✨ Funcionalidades
- 🧮 Geração de uma pirâmide numérica baseada no número de linhas informado pelo usuário.
- ⚙️ Parâmetro opcional que permite configurar o comportamento da impressão (crescimento da pirâmide).

## 🖥️ Exemplo de Uso
### 🔢 Entrada do Usuário:
```plaintext
Digite um número: 5
```
## 📋 Saída Gerada:

- 1
- 1 2
- 1 2 3
- 1 2 3 4
- 1 2 3 4 5

## 🛠️ Como Funciona
### O programa utiliza dois laços for:

- ➡️ O primeiro loop controla o número de linhas.
- ➡️ O segundo loop imprime os números de 1 até o número da linha atual.

## 📂 Estrutura do Código
- 🏷️ A função principal é piramide_com_parametro(n, crescente=True).
n define o número de linhas da pirâmide.
crescente é um parâmetro opcional que, por padrão, é True e controla a geração da pirâmide.

## 🚀 Como Executar
- ✅ Certifique-se de ter o Python instalado em sua máquina (versão 3.x ou superior).
- 📥 Baixe ou copie o código para um arquivo chamado piramide.py.
- ▶️ Execute o arquivo no terminal com o comando:
```python
python piramide.py
```
- 🖊️ Insira um número quando solicitado e veja a pirâmide gerada.

## 🖌️ Personalização
### Se desejar modificar o comportamento do programa:

- 🔄 Altere o parâmetro crescente na chamada da função:
```python
piramide_com_parametro(5, crescente=True)
```
- 🌟 Você pode implementar outras funcionalidades, como pirâmides invertidas ou decorativas.

## 🛠️ Requisitos do Sistema
- 🐍 Python 3.x ou superior.

## 👤 Autor
Este script foi criado como um exemplo didático para ensinar conceitos básicos de loops e funções em Python. 🧠💡 Sinta-se à vontade para modificar e compartilhar.