# Conjuntos de exemplo
clientes_A = {"Alice", "Bob", "Charlie", "David"}  # Conjunto de clientes A
clientes_B = {"Charlie", "David", "Eve", "Frank"}  # Conjunto de clientes B

# Clientes em ambos os conjuntos (interseção)
clientes_em_ambos = clientes_A.intersection(clientes_B)
print("Clientes em ambos os conjuntos:", clientes_em_ambos)

# Clientes apenas no conjunto A (diferença de A para B)
clientes_apenas_A = clientes_A.difference(clientes_B)
print("Clientes apenas no conjunto A:", clientes_apenas_A)

# Clientes apenas no conjunto B (diferença de B para A)
clientes_apenas_B = clientes_B.difference(clientes_A)
print("Clientes apenas no conjunto B:", clientes_apenas_B)

# Todos os clientes únicos (união)
clientes_unicos = clientes_A.union(clientes_B)

# Cálculo da porcentagem de clientes únicos
total_clientes = len(clientes_A) + len(clientes_B)  # Total de clientes somados
percentual_unicos = (len(clientes_unicos) / total_clientes) * 100  # Porcentagem de únicos
print(f"Porcentagem de clientes únicos: {percentual_unicos:.1f}%")
