
representacao_mensal = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}


valor_total_mensal = sum(representacao_mensal.values())


percentuais = {}
for estado, valor in representacao_mensal.items():
    percentual = (valor / valor_total_mensal) * 100
    percentuais[estado] = percentual


print("Percentual de representação por estado:")
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")