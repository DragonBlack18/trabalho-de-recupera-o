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