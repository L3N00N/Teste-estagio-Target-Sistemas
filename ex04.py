# Define o faturamento mensal de cada estado
faturamento_sp = 67836.43
faturamento_rj = 36678.66
faturamento_mg = 29229.88
faturamento_es = 27165.48
faturamento_outros = 19849.53

# Calcula o valor total do faturamento mensal
total_faturamento = faturamento_sp + faturamento_rj + faturamento_mg + faturamento_es + faturamento_outros

# Calcula o percentual de representação de cada estado no faturamento mensal
percentual_sp = faturamento_sp / total_faturamento * 100
percentual_rj = faturamento_rj / total_faturamento * 100
percentual_mg = faturamento_mg / total_faturamento * 100
percentual_es = faturamento_es / total_faturamento * 100
percentual_outros = faturamento_outros / total_faturamento * 100

# Imprime o resultado
print("Percentual de representação do faturamento mensal por estado:")
print(f"SP: {percentual_sp:.2f}%")
print(f"RJ: {percentual_rj:.2f}%")
print(f"MG: {percentual_mg:.2f}%")
print(f"ES: {percentual_es:.2f}%")
print(f"Outros: {percentual_outros:.2f}%")