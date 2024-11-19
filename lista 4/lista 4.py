# Função para gerar a pirâmide
def piramide_com_parametro(n, crescente=True):
    # Verifica se o parâmetro 'crescente' é True
    if crescente:
        # Loop externo para controlar as linhas da pirâmide
        for i in range(1, n + 1):
            # Loop interno para controlar os números de cada linha
            for j in range(1, i + 1):
                # Imprime os números da linha atual, separados por espaço
                print(j, end=" ")
            # Após imprimir todos os números da linha, pula para a próxima linha
            print()

# Solicita ao usuário um número para o tamanho da pirâmide
numero = int(input("Digite um número: "))

# Chama a função para imprimir a pirâmide
piramide_com_parametro(numero)
