import json

with open('faturamento.json', 'r') as file:
    faturamento = json.load(file)

menor_valor = float('inf')
maior_valor = float('-inf')
soma_faturamento = 0
dias_com_faturamento = 0

for dia in faturamento:
    valor = dia['valor']

    if valor > 0:
        if valor < menor_valor:
            menor_valor = valor
        if valor > maior_valor:
            maior_valor = valor
        soma_faturamento += valor
        dias_com_faturamento += 1

media_faturamento = soma_faturamento / dias_com_faturamento

dias_acima_da_media = sum(1 for dia in faturamento if dia['valor'] > media_faturamento)

print(f"Menor valor de faturamento ocorrido em um dia do mês: {menor_valor}")
print(f"Maior valor de faturamento ocorrido em um dia do mês: {maior_valor}")
print(f"Número de dias no mês com faturamento diário superior à média mensal: {dias_acima_da_media}")
