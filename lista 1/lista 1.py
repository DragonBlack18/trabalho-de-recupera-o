# Solicita o peso e a altura do usuário
peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))

# Calcula o IMC usando a fórmula
imc = peso / (altura ** 2)

# Exibe o resultado formatado com duas casas decimais
print(f"IMC: {imc:.2f}")
