
faturamento_diario = [22174.1664, 24537.6698, 26139.6134, 0.0, 0.0, 26742.6612, 0.0, 42889.2258, 46251.174, 11191.4722, 0.0, 0.0, 3847.4823, 373.7838, 2659.7563, 48924.2448, 18419.2614, 0.0, 0.0,35240.1826, 43829.1667,18235.6852, 4355.0662, 13327.1025, 0.0, 0.0, 25681.8318, 1718.1221, 13220.495, 8414.61]
faturamento_diario.remove(0.0)
# Calcula o menor valor de faturamento diário
menor_faturamento = min(faturamento_diario)

# Calcula o maior valor de faturamento diário
maior_faturamento = max(faturamento_diario)

# Calcula a média mensal de faturamento
media_mensal = sum(faturamento_diario) / len(faturamento_diario)

# Calcula o número de dias em que o faturamento diário foi superior à média mensal
dias_acima_da_media = len([faturamento for faturamento in faturamento_diario if faturamento > media_mensal])

# Imprime os resultados
print("Menor faturamento diário:", menor_faturamento)
print("Maior faturamento diário:", maior_faturamento)
print("Dias acima da média mensal:", dias_acima_da_media)




    