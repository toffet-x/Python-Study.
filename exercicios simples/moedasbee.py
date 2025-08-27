# Leitura do valor monetário
valor = float(input())

# Notas e moedas disponíveis
notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

# Cálculo das notas
print("NOTAS:")
for nota in notas:
    quantidade_notas = int(valor // nota)
    valor -= quantidade_notas * nota
    print(f"{quantidade_notas} nota(s) de R$ {nota:.2f}")

# Cálculo das moedas
print("MOEDAS:")
for moeda in moedas[:-1]:  # Exclui a moeda de 1 centavo temporariamente
    quantidade_moedas = int(valor // moeda)
    valor -= quantidade_moedas * moeda
    valor = round(valor, 2)  # Ajuste para evitar problemas de precisão
    print(f"{quantidade_moedas} moeda(s) de R$ {moeda:.2f}")

# Tratamento especial para a moeda de 1 centavo
quantidade_moedas = int(round(valor / 0.01))
valor -= quantidade_moedas * 0.01
print(f"{quantidade_moedas} moeda(s) de R$ 0.01")


