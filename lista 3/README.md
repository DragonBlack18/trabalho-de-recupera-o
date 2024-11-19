# 🧮 Números Primos entre 1 e N

Bem-vindo ao projeto **Números Primos**! Este é um script em Python que recebe um número inteiro do usuário e exibe todos os números primos entre 1 e esse número. 🥳

> **Números primos** são aqueles que possuem apenas dois divisores: o número 1 e eles mesmos. Eles são fundamentais na matemática e na criptografia, sendo uma excelente maneira de explorar loops e estruturas de controle em Python! 🚀

## 📋 Sobre o Projeto

Este projeto é simples, mas poderoso 💪! Ele:
- Recebe um número limite `N` fornecido pelo usuário.
- Verifica cada número de 1 até `N` e identifica quais são primos.
- Exibe todos os números primos encontrados de forma organizada.

## 🛠️ Pré-requisitos

Você só precisa ter o Python instalado em sua máquina para rodar este script! 🐍

## 🚀 Como Usar

Siga as etapas abaixo para executar o script e encontrar todos os números primos até o limite que você escolher!

1. **Clone este repositório** (ou copie o código para sua máquina).
2. **Execute o script** no terminal ou em qualquer IDE de sua preferência.
3. **Digite o limite desejado** quando solicitado, e o programa exibirá os números primos entre 1 e esse limite.

### 📜 Exemplo de Uso

```plaintext
Digite o número limite: 10

2 é primo
3 é primo
5 é primo
7 é primo
``` 
## 🧩 Estrutura do Código

O código utiliza um laço for aninhado para verificar se um número é primo. Cada número é testado para verificar se ele é divisível por qualquer número menor que ele. Se não for divisível por nenhum outro número além de 1 e ele mesmo, ele é considerado primo. ✅

## 🌟 Funcionalidades
- Entrada de Dados: O usuário insere um número limite para a verificação.
- Verificação de Primalidade: O código verifica se cada número no intervalo é primo.
- Exibição dos Resultados: Os números primos são impressos no console.

## 🔧 Código Completo

```python
# Solicita ao usuário o número limite
n = int(input("Digite o número limite: "))

# Percorre todos os números de 2 até o número limite
for i in range(2, n + 1):
    # Assume que o número é primo
    primo = True
    # Verifica se o número é divisível por algum número menor que ele
    for j in range(2, i):
        if i % j == 0:
            primo = False  # Marca como não primo
            break  # Encerra o laço, pois já encontrou um divisor
    # Se o número for primo, imprime na tela
    if primo:
        print(f"{i} é primo")
```

## 📈 Complexidade

O algoritmo possui uma complexidade de tempo de aproximadamente O(N²), onde N é o limite superior definido pelo usuário. Para limites muito grandes, podem ser aplicadas otimizações (como verificar divisores até a raiz quadrada do número) ou usar algoritmos mais avançados para encontrar primos.

## 🧠 Curiosidades Matemáticas

- O número 2 é o único número primo par.
Primos são infinitos, e há padrões complexos em sua distribuição.
- A primalidade é crucial para a segurança em sistemas criptográficos modernos! 

## 🔒🤝 Contribuições

Sinta-se à vontade para abrir issues, propor melhorias ou compartilhar suas próprias implementações do código! 💡

## 📜 Licença

Este projeto é de domínio público e pode ser utilizado livremente. 🌍