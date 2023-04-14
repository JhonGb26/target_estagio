import json

with open('dados.json', 'r') as file:
    dados = json.load(file)


valores_faturamento = [dado['valor'] for dado in dados if dado['valor'] != 0]


menor_valor = min(valores_faturamento)


maior_valor = max(valores_faturamento)


faturamento_total = sum(valores_faturamento)
dias_com_faturamento = len(valores_faturamento)
media_mensal = faturamento_total / dias_com_faturamento


dias_acima_media = sum(1 for valor in valores_faturamento if valor > media_mensal)


print("Menor valor do faturamento ocorrido em um dia do mês: R$", menor_valor)
print("Maior valor do faturamento ocorrido em um dia do mês: R$", maior_valor)
print("Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: ", dias_acima_media)