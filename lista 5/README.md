# 📊 Gerenciamento de Conjuntos de Dados
Sistema em Python para gerenciar e analisar conjuntos de clientes com foco em interseções, diferenças e cálculo de percentuais únicos! 🚀

## 🌟 Funcionalidades Principais
- 📍 Identificar clientes que estão em ambos os conjuntos.
- ➕ Identificar clientes exclusivos do conjunto A.
- ➖ Identificar clientes exclusivos do conjunto B.
- 📊 Calcular a porcentagem de clientes únicos.
## 💡 Como Funciona?
🔑 Entradas
#### Dois conjuntos definidos no código:📊
```
clientes_A = {"Alice", "Bob", "Charlie", "David"}
clientes_B = {"Charlie", "David", "Eve", "Frank"}
```
🎯 Saídas
- Clientes em ambos os conjuntos: 'Charlie', 'David'.
- Clientes exclusivos de A: 'Alice', 'Bob'.
- Clientes exclusivos de B: 'Eve', 'Frank'.
Porcentagem de clientes únicos: `75.0%`.

## 🛠️ Explicação do Código
### 1️⃣ Interseção de Conjuntos
- Usa a função intersection para encontrar clientes em ambos os conjuntos:
```
clientes_em_ambos = clientes_A.intersection(clientes_B)
```

### 2️⃣ Diferença de A para B
- Clientes exclusivos do conjunto A:
```
clientes_apenas_A = clientes_A.difference(clientes_B)
```

### 3️⃣ Diferença de B para A
- Clientes exclusivos do conjunto B:
```
clientes_apenas_B = clientes_B.difference(clientes_A)
```

### 4️⃣ União e Porcentagem de Únicos
- União dos conjuntos para identificar todos os clientes únicos e calcular sua proporção:
```
clientes_unicos = clientes_A.union(clientes_B)
percentual_unicos = (len(clientes_unicos) / (len(clientes_A) + len(clientes_B))) * 100
```

## 🚀 Como Usar?
- Copie o código para um arquivo Python, como gerenciamento_conjuntos.py.
- Altere os conjuntos clientes_A e clientes_B para testar diferentes combinações.

### Execute no terminal:
```
python gerenciamento_conjuntos.py
```

## 📊 Exemplo de Saída no Terminal
```
Clientes em ambos os conjuntos: {'Charlie', 'David'}
Clientes apenas no conjunto A: {'Alice', 'Bob'}
Clientes apenas no conjunto B: {'Eve', 'Frank'}
Porcentagem de clientes únicos: 75.0%
```

## 🖥️ Personalização
- Altere os conjuntos no código para testar com outros dados:
```
clientes_A = {"Maria", "José", "Ana"}
clientes_B = {"José", "Carlos", "Beatriz"}
```
🎉 Exploração garantida!

## Feito com ❤️ e Python 🐍.
Por [Davi Brand]. 🚀