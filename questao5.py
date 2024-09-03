def invert(texto):
    textInvert = ""
    
    for i in range(len(texto) -1, -1, -1):
        textInvert += texto[i]
    
    return textInvert

textOriginal = input("Digite a Palavra:")
textInvert = invert(textOriginal)

print(f"Texto invertido: {textInvert}")
