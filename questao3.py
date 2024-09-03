import json
with open('questao3.json', 'r') as file:
    dados = json.load(file)

min = float('inf')
max = float('-inf')
soma = 0
day = int()

for item in dados:
    if 'valor' in item:
        if item ['valor'] < min:
            min = item['valor']

for item in dados:
    if 'valor' in item:
        if item ['valor'] > max:
            max = item['valor']

for item in dados:
    if 'valor' in item:
        soma += item['valor']

for item in dados:
    if 'dia' in item:
        if item ['dia'] > day:
            day = item ['dia']

media = soma / day

valorPDia = []

for item in dados:
    if 'valor' in item:
        if item ['valor'] > media:
            valorPDia.append(item['valor'])
            QuantDias = len(valorPDia)


print ("Menor valor de faturamento no mês:", min)
print ("Maior valor de faturamento no mês:", max)
print ("Número de dias no mês em que o faturamento foi superior à média mensal:", QuantDias)
