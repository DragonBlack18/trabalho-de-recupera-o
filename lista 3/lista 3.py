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

