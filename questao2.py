indice = 100
contagem = 0
numberOne = 0
numberTwo = 1
num_encontrados = [0,1]
result = 0

while contagem < indice :
    contagem += 1
    result = numberOne + numberTwo
    num_encontrados.append(result)
    numberOne = numberTwo
    numberTwo = result

number = int(input("Escreva o numero:"))

if  number in num_encontrados :
    print("Seu numero é Fibonacci!")
else:
    print("Seu numero não é Fibonacci!")
